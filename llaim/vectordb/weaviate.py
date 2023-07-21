import weaviate
from constants.vectordb import RETRIEVAL_CONFIG_VECTORDB
from langchain.vectorstores.weaviate import Weaviate as LangChainWeaviate


class Weaviate:
    def __init__(self, config: dict) -> None:
        """
        A wrapper around the weaviate-client and langchain's weaviate class

        Args:
            config: Pass the parsed config file into this class
        """
        self.config = config
        self.vectordb_config, self.vectordb_config_fields = self.transform_config()

    def transform_config(self):
        vectordb_config = self.config.get(RETRIEVAL_CONFIG_VECTORDB, None)
        if not vectordb_config:
            raise ValueError("Vector db information not available in retrieval config")

        vectordb_config_fields = vectordb_config.get("fields", None)
        if not vectordb_config_fields:
            raise ValueError("Cannot connect to vector db without compulsory fields like 'url' and 'clause_text' ")
        return vectordb_config, vectordb_config_fields

    def create_weaviate_client(self):
        return weaviate.Client(url=self.vectordb_config_fields.get("url"))

    def get_langchain_client(self):
        return LangChainWeaviate(
            self.create_weaviate_client(),
            self.vectordb_config.get("class_name"),
            self.vectordb_config_fields.get("text_key"),
        )
