import typing, os
import tempfile

from langchain.vectorstores.chroma import Chroma as LangchainChroma
from langchain.embeddings import HuggingFaceEmbeddings
from chromadb import PersistentClient
from langchain.docstore.document import Document

from .base import BaseVectordb


MEMORY_INDEX_NAME = "MemoryIndex"


class ChromaDB(BaseVectordb):
    required_fields = ["class_name"]

    def _get_persistent_path(self):
        return os.path.join(tempfile.gettempdir(), "llmstack")

    def create_client(self):
        return PersistentClient(
            path=self.vectordb_config_fields.get("persistent_file_path") or self._get_persistent_path()
        )

    def get_langchain_client(self):
        return LangchainChroma(
            collection_name=self.vectordb_config.get("class_name"),
            client=self.create_client(),
            embedding_function=self.get_embedding(),
        )

    def search(self, query: str) -> typing.List[Document]:
        langchain_faiss_client = self.get_langchain_client()
        return langchain_faiss_client.similarity_search(query)

    def get_langchain_memory_client(self):
        return LangchainChroma(
            collection_name=MEMORY_INDEX_NAME, client=self.create_client(), embedding_function=self.get_embedding()
        )
