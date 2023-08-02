from typing import List

import weaviate
from langchain.docstore.document import Document
from langchain.vectorstores.weaviate import Weaviate as LangChainWeaviate
from weaviate.exceptions import UnexpectedStatusCodeException


from .base import BaseVectordb


MEMORY_INDEX_NAME = "MemoryIndex"  # Weaviate requires index names to be in PascalCase
MEMORY_TEXT_KEY = "chat_history"


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

    def _check_text_key(self, client) -> None:
        text_key = self.vectordb_config_fields.get("text_key")
        class_schema = client.schema.get(self.vectordb_config.get("class_name"))
        available_text_keys = [prop["name"] for prop in class_schema["properties"]]

        if text_key not in available_text_keys:
            raise ValueError(
                f"The text key {text_key} you specified in the vector db is not available. Please choose from one of these text_key {available_text_keys}"
            )

    def get_langchain_client(self) -> LangChainWeaviate:
        client = self.create_client()
        self._check_text_key(client)
        return LangChainWeaviate(
            client,
            self.vectordb_config.get("class_name"),
            self.vectordb_config_fields.get("text_key"),
        )

    def get_langchain_memory_client(self) -> LangChainWeaviate:
        client = self.create_client()
        self._setup_vectordb_memory(client=client)
        return LangChainWeaviate(client, index_name=MEMORY_INDEX_NAME, text_key=MEMORY_TEXT_KEY)

    def _setup_vectordb_memory(self, client: weaviate.Client):
        """
        Get or Create a vectordb index
        """
        try:
            client.schema.get(class_name=MEMORY_INDEX_NAME)
        except UnexpectedStatusCodeException:
            print("Creating memory index class in vector db")
            client.schema.create_class(
                {
                    "class": MEMORY_INDEX_NAME,
                    "properties": [
                        {"name": MEMORY_TEXT_KEY, "dataType": ["text"]},
                    ],
                }
            )
