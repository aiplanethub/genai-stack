from llaim.constants import VECTOR_DB_CLIENT_MAP, VectorDB
from llaim.config import ConfigLoader
from vectordb.base import BaseVectordb
from typing import Any


class BaseRetriever(ConfigLoader):
    module_name = "BaseRetriever"
    config_key = "retriever"

    def __init__(self, config: str):
        super().__init__(self.module_name, config)
        self.parse_config(self.config_key, self.compulsory_fields)
        self.vector_store_client = self._get_vector_store_client()

    def _get_vector_store_client_class(self):
        vector_store_client_class = VECTOR_DB_CLIENT_MAP.get(self.config.get(), None)
        if not self.vector_store_client:
            raise ValueError(
                f"Client not found for the specified vectordb {self.vector_store}. Available VectorDBs are {[db.value for db in VectorDB]}"
            )
        return vector_store_client_class

    def _get_vector_store_client(self) -> BaseVectordb:
        vector_store_class = self._get_vector_store_client_class()
        return vector_store_class(self.config)

    def retrieve(self, query: Any):
        raise NotImplementedError()
