from .base import BaseRetriever


class LangChainRetriever(BaseRetriever):
    def retrieve(self):
        self.vector_store_client
