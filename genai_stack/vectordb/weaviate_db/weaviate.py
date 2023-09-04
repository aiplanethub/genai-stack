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
        db_parameters = self.config.data_model

        # Initialize weaviate client
        weaviate_client_init_params = extract_class_init_attrs(weaviate.Client)
        client_init_params = self.sanitize_params_dict(
            weaviate_client_init_params,
            dict(db_parameters),
        )

        self.client = weaviate.Client(**client_init_params)

        # Initialize Langchain Client
        init_params = extract_class_init_attrs(LangChainWeaviate)
        lc_init_params = self.sanitize_params_dict(
            init_params,
            dict(db_parameters),
        )

        self.lc_client = LangChainWeaviate(
            client=self.client,
            **lc_init_params,
        )

    def create_index(self, index_name: str, text_key: Optional[str] = "default_key", **kwargs):
        """
        Get or Create a vectordb index
        """
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
    
    @property
    def client(self) -> weaviate.Client:
        return self._client

    @client.setter
    def client(self, db_client: weaviate.Client):
        self._client = db_client

    def search_method(self, query: str):
        search_methods = {"similarity_search": self.similarity_search, "max_marginal_relevance_search": self.mmr}
        self._search_method = search_methods.get(self.config.search_method)(query=query)

    def similarity_search(self, query: str):
        return self.lc_client.similarity_search(
            query=query,
            **self.search_options,
        )

    def mmr(self, query: str):
        return self.lc_client.max_marginal_relevance_search(query=query, **self.search_options)

    def search(self, query: str):
        return self.search_method(query)

    