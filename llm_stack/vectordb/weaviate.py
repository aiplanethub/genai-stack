from typing import List

import weaviate
from langchain.docstore.document import Document
from langchain.vectorstores.weaviate import Weaviate as LangChainWeaviate

from .base import BaseVectordb


class Weaviate(BaseVectordb):
    required_fields = ["url", "class_name", "text_key"]

    def create_client(self):
        client_params = {"url": self.vectordb_config_fields.get("url")}
        if api_key := self.vectordb_config_fields.get("api_key"):
            client_params["auth_config"] = weaviate.AuthApiKey(api_key=api_key)
        return weaviate.Client(**client_params)

    def search(self, query: str) -> List[Document]:
        langchain_weaviate_client = self.get_langchain_client()
        return langchain_weaviate_client.similarity_search_by_text(query=query)

    def get_langchain_client(self) -> LangChainWeaviate:
        return LangChainWeaviate(
            self.create_client(),
            self.vectordb_config.get("class_name"),
            self.vectordb_config_fields.get("text_key"),
        )
