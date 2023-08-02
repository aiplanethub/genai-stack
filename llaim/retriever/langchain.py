from .base import BaseRetriever


class LangChainRetriever(BaseRetriever):
    def retrieve(self, query):
        vectordb = self.vectordb
        return vectordb.search(query)
