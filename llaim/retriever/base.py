from llaim.constants import VECTOR_DB_CLIENT_MAP, VectorDB
from llaim.config import ConfigLoader
from vectordb.base import BaseVectordb
from typing import Any


class BaseRetriever(ConfigLoader):
    module_name = "BaseRetriever"
    config_key = "retriever"

    def __init__(self, config: str, vectordb: BaseVectordb = None):
        super().__init__(self.module_name, config)
        self.parse_config(self.config_key, self.compulsory_fields)
        self.vectordb = self.vectordb

    def retrieve(self, query: Any):
        raise NotImplementedError()
