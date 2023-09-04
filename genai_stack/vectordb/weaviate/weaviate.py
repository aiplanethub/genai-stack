from typing import Iterable, List

import weaviate
from langchain.docstore.document import Document
from langchain.vectorstores.weaviate import Weaviate as LangChainWeaviate
from weaviate.exceptions import UnexpectedStatusCodeException

from genai_stack.vectordb.weaviate import WeaviateDBConfig
from genai_stack.vectordb.base import BaseVectorDB
from genai_stack.utils.extraction import extract_class_init_attrs

MEMORY_INDEX_NAME = "MemoryIndex"  # Weaviate requires index names to be in PascalCase
MEMORY_TEXT_KEY = "chat_history"


class Weaviate(BaseVectorDB):
    config_class = WeaviateDBConfig
    _client: weaviate.Client = None

    # def create_client(self):
    #     client_params = {"url": self.vectordb_config_fields.get("url")}
    #     if api_key := self.vectordb_config_fields.get("api_key"):
    #         client_params["auth_config"] = weaviate.AuthApiKey(api_key=api_key)
    #     return weaviate.Client(**client_params)
    def _sanitize_params_dict(self, params_dict, source_dict, sanitized_dict):
        params_dict.pop("args", None)
        params_dict.pop("kwargs", None)
        for key, val in params_dict.items():
            param_val = source_dict.get("fields", {}).get(key)
            if val and param_val or not val:
                sanitized_dict[key] = param_val
        return sanitized_dict

    def _post_init(self, *args, **kwargs):
        db_parameters = self.config.data_model

        # Initialize weaviate client
        weaviate_client_init_params = extract_class_init_attrs(weaviate.Client)
        sanitized_init_params = {}
        self._sanitize_params_dict(
            weaviate_client_init_params,
            db_parameters.__dict__,
            sanitized_init_params,
        )

        self.client = weaviate.Client()

        # Initialize Langchain Client
        init_params = extract_class_init_attrs(LangChainWeaviate)
        sanitized_init_params = {}
        self._sanitize_params_dict(
            init_params,
            self.search_options,
            sanitized_init_params,
        )

        self.lc_chroma = LangChainWeaviate(
            client=self.client,
            **sanitized_init_params,
        )

    @property
    def client(self) -> weaviate.Client:
        return self._client

    @client.setter
    def client(self, db_client: weaviate.Client):
        self._client = db_client

    def search(self, query: str) -> List[Document]:
        langchain_weaviate_client = self.get_langchain_client()
        return langchain_weaviate_client.similarity_search_by_text(query=query)

    def _check_text_key(self, client) -> None:
        text_key = self.vectordb_config_fields.get("text_key")
        class_schema = client.schema.get(
            self.vectordb_config.get(
                "class_name",
                "",
            ).capitalize()
        )
        available_text_keys = [prop["name"] for prop in class_schema["properties"]]

        if text_key not in available_text_keys:
            raise ValueError(
                f"The text_key '{text_key}' you specified in the vector db config is not available. Please choose from one of these text_key {available_text_keys}"
            )

    def get_langchain_client(self) -> LangChainWeaviate:
        client = self.create_client()
        self._check_text_key(client)
        return LangChainWeaviate(
            client,
            self.vectordb_config.get("class_name").capitalize(),
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
