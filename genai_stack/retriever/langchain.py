from .base import BaseRetrieverConfigModel, BaseRetrieverConfig, BaseRetriever
from genai_stack.retriever.utils import parse_search_results


class LangChainConfigModel(BaseRetrieverConfigModel):
    """
    Data Model for the configs
    """
    pass


class LangChainConfig(BaseRetrieverConfig):
    data_model = LangChainConfigModel


class LangChain(BaseRetriever):
    config_class = LangChainConfig

    def retrieve(self, query:str): 

        prompt_template = self.get_prompt(query=query)

        prompt_dict = {
            "history": self.get_chat_history(),
            "context": self.get_context(query=query),
            "query": query
        }

        final_prompt_template =  prompt_template.template.format(
            **{k:v for k,v in prompt_dict.items() if k in prompt_template.input_variables}
        )

        return self.mediator.get_model_response(prompt=final_prompt_template)

    def get_context(self, query: str):
        context = self.mediator.search_vectordb(query=query)
         
        return parse_search_results(context)
    

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
