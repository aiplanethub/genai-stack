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
        client_init_params = sanitize_params_dict(
            weaviate_client_init_params,
            dict(db_parameters),
        )

        self.client = weaviate.Client(**client_init_params)

        # Initialize Langchain Client
        init_params = extract_class_init_attrs(LangChainWeaviate)
        lc_init_params = sanitize_params_dict(
            init_params,
            dict(db_parameters),
        )

        self.lc_client = self._create_langchain_client(**lc_init_params)

    def _create_langchain_client(self, **kwargs):
        return LangChainWeaviate(client=self.client, embedding=self.mediator.get_embedding_function(), **kwargs)

    def add_texts(self, source_docs):
        return self.lc_client.add_documents(source_docs)

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

    @property
    def client(self) -> weaviate.Client:
        return self._client

    @client.setter
    def client(self, db_client: weaviate.Client):
        self._client = db_client

    def search_method(self, query: str):
        search_methods = {"similarity_search": self.similarity_search, "max_marginal_relevance_search": self.mmr}
        search_results = search_methods.get(self.config.search_method)(query=query)
        return search_results

    def similarity_search(self, query: str):
        """
        Return docs based on similarity search

        Args:
            query: Document or string against which you want to do the search
        """

        return self.lc_client.similarity_search(
            query=query,
            **self.search_options,
        )

    def mmr(self, query: str):
        """
        Return docs selected using the maximal marginal relevance.
        Maximal marginal relevance optimizes for similarity to query AND diversity
        among selected documents.

        Args:
            query: Document or string against which you want to do the search
        """
        return self.lc_client.max_marginal_relevance_search(query=query, **self.search_options)

    def search(self, query: str):
        return self.search_method(query)
