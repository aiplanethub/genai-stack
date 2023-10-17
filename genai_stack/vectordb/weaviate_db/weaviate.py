from typing import Optional, List

import weaviate
from langchain.vectorstores.weaviate import Weaviate as LangChainWeaviate
from weaviate.exceptions import UnexpectedStatusCodeException
from langchain.docstore.document import Document

from genai_stack.vectordb.utils import HybridSearchResponse
from genai_stack.vectordb.weaviate_db import WeaviateDBConfig
from genai_stack.vectordb.base import BaseVectorDB
from genai_stack.utils.extraction import extract_class_init_attrs
from genai_stack.utils.sanitize import sanitize_params_dict
from genai_stack.memory.utils import parse_weaviate_chat_conversations


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
    ) -> List[HybridSearchResponse]:
        if kwargs.get("attributes", None):
            kwargs['attributes'] += self.config.config_data.attributes
        args = {
            "query": query,
            "k": k
        }
        if metadata:
            where_filter = {
                "operator": "And",
                "operands": [
                    {
                        "path": [key],
                        "operator": "Equal",
                        "valueString": value,
                    } if type(value) == str else {
                        "path": [key],
                        "operator": "Equal",
                        "valueNumber": value,
                    } for key, value in metadata.items()
                ]
            }
            args["where_filter"] = where_filter
        lc_client = self._create_langchain_client(**kwargs)
        documents = lc_client.similarity_search_with_score(**args)
        return [HybridSearchResponse(
            query=document[0].page_content,
            response=document[0].metadata.get("response") if document[0].metadata else None,
            score=document[1],
            isSimilar=document[1] > 0.90,
            document=document[0],
        ) for document in documents]

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
            self.client.schema.create_class(class_schema)
        return self._create_langchain_client(index_name=index_name, text_key=text_key)
    
    def get_vectordb_chat_history(self, k, **kwargs):
        index_name = kwargs.get('index_name')
        text_key = kwargs.get('text_key')

        documents = self.lc_client._client.query.get(
            class_name=index_name,
            properties=[text_key]
        ).with_additional(["id"]).do()['data']['Get'][index_name]
        
        return parse_weaviate_chat_conversations(
            search_results=documents, 
            text_key=text_key
        )
    
    def add_chat_conversation(self, user_text, model_text, **kwargs):

        index_name = kwargs.get('index_name')
        text_key = kwargs.get('text_key')

        db = self.lc_client._client

        conversations = db.query.get(
            class_name=index_name,
            properties=[text_key]
        ).with_additional(["id"]).do()['data']['Get'][index_name]

        new_conversation = f"HUMAN: {user_text}\nYOU: {model_text}"

        if len(conversations) == 0:
            # creating a object
            db.data_object.create(
                data_object={text_key:new_conversation},
                class_name=index_name,
            )
        else:
            # updating the retrieved object by appending the new conversation
            db.data_object.update(
                uuid=conversations[0].get("_additional").get("id"),
                class_name=index_name,
                data_object={
                    text_key:conversations[0].get(text_key)+"\n\n"+new_conversation
                }
            )
