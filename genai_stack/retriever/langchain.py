from typing import List
from langchain.docstore.document import Document

from .base import BaseRetrieverConfigModel, BaseRetrieverConfig, BaseRetriever


class LangChainConfigModel(BaseRetrieverConfigModel):
    name:str


class LangChainConfig(BaseRetrieverConfig):
    data_model = LangChainConfigModel


class LangChain(BaseRetriever):
    config_class = LangChainConfig

    def retrive(self): 
        prompt_template = self.get_prompt()

        context = self.get_context(prompt_template)  

        conversation_history = ""

        new_prompt_template = f"{prompt_template} {context} {conversation_history}"

        return new_prompt_template

    def get_context(self, query: str):

        if not self._mediator._stack.vectordb:
            raise ValueError("VectorDB component is not provided, Retriever component require a vectordb component.")
        
        vectorDB = self._mediator._stack.vectordb

        return self.parse_search_results(vectorDB.search(query))
    
    def parse_search_results(self, search_results: List[Document]):
        """
        This method returns a content extracted from the documents list.
        """
        result = ""

        for idx, search_result in enumerate(search_results):
            result += f"{idx + 1}. {search_result.page_content} \n"

        return result
    
    def get_chat_history(self):

        if not self._mediator._stack.memory:
            raise ValueError("Memory component is not provided, Retriever component require a memory component.")

    @staticmethod
    def config_class() -> LangChainConfig:
        return LangChainConfig
    

# from typing import List
# from langchain.docstore.document import Document

# from .base import BaseRetriever


# class LangChainRetriever(BaseRetriever):
#     required_fields = []

#     def retrieve(self, query):
#         vectordb = self.vectordb
#         return self.parse_search_results(vectordb.search(query))

#     def parse_search_results(self, search_results: List[Document]):
#         result = ""

#         for idx, search_result in enumerate(search_results):
#             result += f"{idx + 1}. {search_result.page_content} \n"

#         return result
