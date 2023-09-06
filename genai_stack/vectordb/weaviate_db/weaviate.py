from typing import Optional

import weaviate
from langchain.docstore.document import Document
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
        return LangChainWeaviate(client=self.client, embedding=self.mediator.get_embedding_function(), **kwargs)

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
