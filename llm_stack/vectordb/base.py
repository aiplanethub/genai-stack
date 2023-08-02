from typing import List

from langchain.docstore.document import Document
from llm_stack.config import ConfigLoader
from llm_stack.constants.vectordb import VECTORDB_CONFIG_KEY


class BaseVectordb(ConfigLoader):
    module_name = "VectorDB"
    config_key = VECTORDB_CONFIG_KEY

    def __init__(self, config: dict) -> None:
        """
        A wrapper around the weaviate-client and langchain's weaviate class

        Args:
            config: Pass the parsed config file into this class
        """
        super().__init__(name=self.module_name, config=config)
        self.parse_config(self.config_key, self.compulsory_fields)

    def search(self, query: str) -> List[Document]:
        raise NotImplementedError()

    def create_client(self):
        raise NotImplementedError()

    def get_langchain_client(self):
        raise NotImplementedError()
