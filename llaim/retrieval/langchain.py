from .base import BaseRetriever

from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain


class LangChainRetriever(BaseRetriever):
    def retrieve(self):
        self.vector_store_client




