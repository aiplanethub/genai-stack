from typing import Optional, List, Union

import weaviate
from langchain.vectorstores.weaviate import Weaviate as LangChainWeaviate
from weaviate.exceptions import UnexpectedStatusCodeException
from langchain.docstore.document import Document

from genai_stack.vectordb.utils import HybridSearchResponse
from genai_stack.vectordb.weaviate_db import WeaviateDBConfig
from genai_stack.vectordb.base import BaseVectorDB
from genai_stack.utils.extraction import extract_class_init_attrs
from genai_stack.utils.sanitize import sanitize_params_dict
from datetime import datetime


class Weaviate(BaseVectorDB):
    config_class = WeaviateDBConfig
    _client: weaviate.Client = None

    def _post_init(self, *args, **kwargs):
        db_parameters = self.config.config_data

        # Initialize weaviate client
        weaviate_client_init_params = extract_class_init_attrs(weaviate.Client)
        client_init_params = sanitize_params_dict(
            weaviate_client_init_params,
            dict(db_parameters),
        )

        self.client = weaviate.Client(**client_init_params)

    @property
    def client(self) -> weaviate.Client:
        return self._client

    @client.setter
    def client(self, db_client: weaviate.Client):
        self._client = db_client

    @property
    def lc_client(self):
        # Get params to be passed for initialization based on the params provided by user
        init_params = extract_class_init_attrs(LangChainWeaviate)
        lc_init_params = sanitize_params_dict(
            init_params,
            dict(self.config.config_data),
        )

        return self._create_langchain_client(**lc_init_params)

    def _create_langchain_client(self, **kwargs):
        return LangChainWeaviate(
            client=self.client,
            embedding=self.mediator.get_embedding_function(),
            by_text=False,
            **kwargs,
        )

    def hybrid_search(
        self,
        query: str,
        metadata: dict,
        k=1,
        **kwargs,
    ) -> List[HybridSearchResponse]:
        if kwargs.get("attributes", None):
            kwargs["attributes"] += self.config.config_data.attributes
        args = {"query": query, "k": k}
        if metadata:
            where_filter = {
                "operator": "And",
                "operands": [
                    {
                        "path": [key],
                        "operator": "Equal",
                        "valueString": value,
                    }
                    if type(value) == str
                    else {
                        "path": [key],
                        "operator": "Equal",
                        "valueNumber": value,
                    }
                    for key, value in metadata.items()
                ],
            }
            args["where_filter"] = where_filter
        lc_client = self._create_langchain_client(**kwargs)
        documents = lc_client.similarity_search_with_score(**args)
        return [
            HybridSearchResponse(
                query=document[0].page_content,
                response=document[0].metadata.get("response")
                if document[0].metadata
                else None,
                score=document[1],
                isSimilar=document[1] > 0.90,
                document=document[0],
            )
            for document in documents
        ]

    def create_index(
        self, index_name: str, text_key: Optional[str] = "default_key", **kwargs
    ):
        try:
            self.client.schema.get(class_name=index_name)
        except UnexpectedStatusCodeException:
            class_schema = {
                "class": index_name,
            }
            if not kwargs.get("properties", None):
                class_schema["properties"] = [
                    {"name": text_key, "dataType": ["text"]},
                ]
            else:
                class_schema["properties"] = kwargs.get("properties")

            self.client.schema.create_class(class_schema)

        kwargs.pop("properties", None)
        return self._create_langchain_client(
            index_name=index_name, text_key=text_key, **kwargs
        )

    def delete_documents(
        self, index_name: str, document_ids: Union[List[str], List[int]]
    ) -> None:
        """
        This method deletes the documents

        Args:
            class_name:str
            document_ids: List[ int | str ]
        """
        client = self.lc_client._client.data_object

        for document_id in document_ids:
            client.delete(class_name=index_name, uuid=document_id)

    def get_documents(self, **kwargs) -> List[Document]:
        """This method returns the list of documents"""

        class_name = kwargs.get("index_name")

        client = self.lc_client._client.query

        rft = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")

        results = (
            client.get(class_name, ["chat_key", "timestamp"])
            .with_where(
                {
                    "path": ["timestamp"],
                    "operator": "LessThan",
                    "valueDate": rft,
                }
            )
            .with_additional(["id"])
            .with_sort(
                {
                    "path": ["timestamp"],
                    "order": "asc",
                }
            )
            .with_limit(40)
            .do()
        )

        docs = [
            Document(
                page_content=doc.get("chat_key"),
                metadata={"id": doc.get("_additional").get("id")},
            )
            for doc in results.get("data").get("Get").get(class_name)
        ]

        if len(docs) == 40:
            # deleting the starting 20 documents and returning last 20 documents.
            doc_ids = [doc.metadata.get("id") for doc in docs[:20]]
            self.delete_documents(class_name, doc_ids)
            return docs[-20:]
        else:
            # returning all documents, max 39 documents.
            return docs

    def create_document(self, document, **kwargs) -> dict:
        """This method creates a new document."""
        class_name = kwargs.get("index_name")

        client = self.lc_client._client.data_object

        datetime_now = datetime.utcnow()
        rfcc = datetime_now.strftime("%Y-%m-%dT%H:%M:%S+00:00")

        client.create(
            class_name=class_name,
            data_object={"chat_key": document, "timestamp": rfcc},
        )
