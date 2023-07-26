from typing import Any

from llaim.constants.vectordb import VectorDB
from llaim.config import ConfigLoader
from llaim.constants.retriever import RETRIEVER_CONFIG_KEY
from llaim.vectordb.base import BaseVectordb


class BaseRetriever(ConfigLoader):
    module_name = "BaseRetriever"
    config_key = RETRIEVER_CONFIG_KEY

    def __init__(self, config: str, vectordb: BaseVectordb = None):
        super().__init__(self.module_name, config)
        self.parse_config(self.config_key, self.compulsory_fields)
        self.vectordb = self.vectordb

    def retrieve(self, query: Any):
        raise NotImplementedError()
