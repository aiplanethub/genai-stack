import weaviate
from config import ConfigLoader
from langchain.vectorstores.weaviate import Weaviate as LangChainWeaviate


class Weaviate(ConfigLoader):
    compulsory_fields = ["url, class_name", "text_key"]

    def create_weaviate_client(self):
        return weaviate.Client(url=self.vectordb_config_fields.get("url"))

    def get_langchain_client(self):
        return LangChainWeaviate(
            self.create_weaviate_client(),
            self.vectordb_config.get("class_name"),
            self.vectordb_config_fields.get("text_key"),
        )
