from typing import List

from langchain.schema import Document

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

    def retrieve(self, query: str, context: List[Document] = None):
        prompt_template = self.get_prompt(query=query)

        prompt_dict = {"query": query}
        metadata = None
        if "context" in prompt_template.input_variables:
            if not context:
                context = self.mediator.search_vectordb(query=query)
            metadata = context[0].metadata if context else None
            prompt_dict['context'] = parse_search_results(context)

        # Cache is given priority over memory
        cache = self.mediator.get_cache(query=query, metadata=metadata)
        if cache:
            return {'output': cache}
        elif "history" in prompt_template.input_variables:
            prompt_dict['history'] = self.get_chat_history(query=query)

        final_prompt_template = prompt_template.template.format(
            **{k: v for k, v in prompt_dict.items()}
        )
        response = self.mediator.get_model_response(prompt=final_prompt_template)
        # Set cache if cache component is there else check for add to memory
        if not self.mediator.set_cache(response=response['output'], query=query, metadata=metadata):
            self.mediator.add_text(user_text=query, model_text=response['output'])
        return response
