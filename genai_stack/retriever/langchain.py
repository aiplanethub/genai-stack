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
            prompt_dict["context"] = parse_search_results(context)
        if "history" in prompt_template.input_variables:
            prompt_dict["history"] = self.get_chat_history()
        else:
            # Cache and memory cannot co-exist. Memory is given priority.
            cache = self.mediator.get_cache(query=query, metadata=metadata)
            if cache:
                return {"output": cache}
        final_prompt_template = prompt_template.template.format(**{k: v for k, v in prompt_dict.items()})
        response = self.mediator.get_model_response(prompt=final_prompt_template)
        self.mediator.add_text(user_text=query, model_text=response["output"])
        if "history" not in prompt_template.input_variables:
            self.mediator.set_cache(response=response["output"], query=query, metadata=metadata)
        return response
