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
        cache = {"query": query}
        if "context" in prompt_template.input_variables:
            context = self.mediator.search_vectordb(query=query)
            cache = self.mediator.get_cache(
                query=query,
                metadata=context[0].metadata
            )
            if cache:
                self.mediator.add_text(user_text=query, model_text=cache['response'])
            cache["metadata"] = context[0].metadata
            prompt_dict['context'] = parse_search_results(context)
        if "history" in prompt_template.input_variables:
            prompt_dict['history'] = self.get_chat_history()

        final_prompt_template =  prompt_template.template.format(
            **{k:v for k,v in prompt_dict.items()}
        )
        response = self.mediator.get_model_response(prompt=final_prompt_template)
        self.mediator.add_text(user_text=query, model_text=response['output'])
        cache["response"] = response['output']
        self.mediator.set_cache(**cache)

        return response

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
