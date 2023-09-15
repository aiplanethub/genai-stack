from typing import Optional

import weaviate
from langchain.vectorstores.weaviate import Weaviate as LangChainWeaviate
from weaviate.exceptions import UnexpectedStatusCodeException

from genai_stack.vectordb.weaviate_db import WeaviateDBConfig
from genai_stack.vectordb.base import BaseVectorDB
from genai_stack.utils.extraction import extract_class_init_attrs
from genai_stack.utils.sanitize import sanitize_params_dict


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
            client=self.client, embedding=self.mediator.get_embedding_function(), by_text=False, **kwargs
        )

    def hybrid_search(
        self,
        query: str,
        metadata: dict,
        k=1,
        **kwargs,
    ):
        where_filter = {
            "operator": "And",
            "operands": [
                {
                    "path": [key],
                    "operator": "Equal",
                    "valueString": value,
                } for key, value in metadata.items()
            ]
        }
        lc_client = self._create_langchain_client(**kwargs)
        documents = lc_client.similarity_search_with_score(
            query=query,
            where_filter=where_filter,
            k=k,
        )
        return [{
            "query": document[0].page_content,
            "response": document[0].metadata.get("response"),
            "score": document[1],
            "isSimilar": document[1] > 0.75,
            "document": document[0],
        } for document in documents]

    def create_index(self, index_name: str, text_key: Optional[str] = "default_key", **kwargs):
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
            if kwargs.get("attributes", None):
                class_schema["properties"][0]["attributes"] = self.config.config_data.attributes + kwargs["attributes"]
            self.client.schema.create_class(class_schema)

        return self._create_langchain_client(index_name=index_name, text_key=text_key)
