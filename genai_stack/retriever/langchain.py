from .base import BaseRetrieverConfigModel, BaseRetrieverConfig, BaseRetriever
from genai_stack.retriever.utils import parse_search_results


class LangChainRetrieverConfigModel(BaseRetrieverConfigModel):
    """
    Data Model for the configs
    """
    pass


class LangChainRetrieverConfig(BaseRetrieverConfig):
    data_model = LangChainRetrieverConfigModel


class LangChainRetriever(BaseRetriever):
    config_class = LangChainRetrieverConfig

    def retrieve(self, query:str): 

        prompt_template = self.get_prompt(query=query)

        prompt_dict = {
            "query": query
        }

        if "context" in prompt_template.input_variables:
            prompt_dict['context'] = self.get_context(query=query)
        
        if "history" in prompt_template.input_variables:
            prompt_dict['history'] = self.get_chat_history()

        final_prompt_template =  prompt_template.template.format(
            **{k:v for k,v in prompt_dict.items()}
        )

        response = self.mediator.get_model_response(prompt=final_prompt_template)

        if "history" in prompt_template.input_variables:
            self.mediator.add_text(user_text=query, model_text=response['output'])

        return response

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
