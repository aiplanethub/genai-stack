from .base import BaseRetriever


class LangChainRetriever(BaseRetriever):
    def retrieve(self, query):
        vector_store = self.vector_store_client
        return vector_store.search(query)
