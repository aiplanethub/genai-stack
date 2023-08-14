from typing import Any

from llm_stack.core import BaseComponent
from llm_stack.constants.retriever import RETRIEVER_CONFIG_KEY
from llm_stack.vectordb.base import BaseVectordb


class BaseRetriever(BaseComponent):
    module_name = "BaseRetriever"
    config_key = RETRIEVER_CONFIG_KEY

    def __init__(self, config: str, vectordb: BaseVectordb = None):
        super().__init__(self.module_name, config)
        self.parse_config(self.config_key, self.required_fields)
        self.vectordb = vectordb

    def retrieve(self, query: Any):
        raise NotImplementedError()

    def get_langchain_retriever(self):
        return self.vectordb.get_langchain_client().as_retriever()

    def get_langchain_memory_retriever(self):
        return self.vectordb.get_langchain_memory_client().as_retriever()

    @classmethod
    def from_config(cls, config):
        raise NotImplementedError
