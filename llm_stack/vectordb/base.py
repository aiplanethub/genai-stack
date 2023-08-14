from typing import List, Any

from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings

from llm_stack.config import ConfigLoader
from llm_stack.utils.importing import import_class
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
        self.parse_config(self.config_key, self.required_fields)

    def search(self, query: str) -> List[Document]:
        raise NotImplementedError()

    def create_client(self):
        raise NotImplementedError()

    def get_langchain_client(self):
        raise NotImplementedError()

    def get_langchain_memory_client(self):
        raise NotImplementedError()

    def store_documents(self, documents: List[Document]):
        client = self.get_langchain_client()
        client.add_documents(documents)

    def _get_default_embedding(self):
        model_name = "sentence-transformers/all-mpnet-base-v2"
        model_kwargs = {"device": "cpu"}
        encode_kwargs = {"normalize_embeddings": False}
        return HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs)

    def get_embedding(self):
        if embedding := self.vectordb_config.get("embedding"):
            embedding_cls = import_class(
                f"langchain.embeddings.{embedding.get('name')}",
            )
            embedding = embedding_cls(**embedding.get("fields"))
        elif not embedding:
            embedding = self._get_default_embedding()
        return embedding

    @classmethod
    def from_config(cls, config):
        raise NotImplementedError
