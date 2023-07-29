from typing import Any

from llm_stack.constants.vectordb import VectorDB
from llm_stack.config import ConfigLoader
from llm_stack.constants.retriever import RETRIEVER_CONFIG_KEY
from llm_stack.vectordb.base import BaseVectordb


class BaseRetriever(ConfigLoader):
    module_name = "BaseRetriever"
    config_key = RETRIEVER_CONFIG_KEY

    def __init__(self, config: str, vectordb: BaseVectordb = None):
        super().__init__(self.module_name, config)
        self.parse_config(self.config_key, self.required_fields)
        self.vectordb = vectordb

    def retrieve(self, query: Any):
        raise NotImplementedError()
