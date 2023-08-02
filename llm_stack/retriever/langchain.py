from typing import List
from langchain.docstore.document import Document

from .base import BaseRetriever


class LangChainRetriever(BaseRetriever):
    required_fields = []

    def retrieve(self, query):
        vectordb = self.vectordb
        return self.parse_search_results(vectordb.search(query))

    def parse_search_results(self, search_results: List[Document]):
        result = ""

        for idx, search_result in enumerate(search_results):
            result += f"{idx + 1}. {search_result.page_content} \n"

        return result
