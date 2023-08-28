from pydantic import BaseModel
from genai_stack.stack.stack_component import StackComponent, StackComponentConfig


class BaseRetrieverConfigModel(BaseModel):
    """
    Data Model for the configs
    """
    pass


class BaseRetrieverConfig(StackComponentConfig):
    data_model = BaseRetrieverConfigModel


class BaseRetriever(StackComponent):
    config_class = BaseRetrieverConfig

    def get_prompt(self):
        """
        This method returns the prompt template from the prompt engine component
        """
        if not self.mediator._stack.prompt_engine:
            raise ValueError("Prompt Engine component is not provided, Retriever component require a prompt engine component.")
        
        return self.mediator._stack.prompt_engine.get_prompt()

    def retrive(self):
        """
        This method returns the prompt template by adding the relevant documents context and chat conversation history
        """
        raise NotImplementedError()
    
    def get_context(self, query:str):
        """
        This method returns the relevant documents returned by the similarity search from a vectordb based on the query
        """
        raise NotImplementedError()
    
    def get_chat_history(self):
        """
        This method returns the chat conversation history
        """
        raise NotImplementedError()

    @staticmethod
    def config_class() -> BaseRetrieverConfig:
        return BaseRetrieverConfig


# from typing import Any

# from genai_stack.core import BaseComponent
# from genai_stack.constants.retriever import RETRIEVER_CONFIG_KEY
# from genai_stack.vectordb.base import BaseVectordb

# class BaseRetriever(BaseComponent):
#     module_name = "BaseRetriever"
#     config_key = RETRIEVER_CONFIG_KEY

#     def __init__(self, config: str, vectordb: BaseVectordb = None):
#         super().__init__(self.module_name, config)
#         self.parse_config(self.config_key, self.required_fields)
#         self.vectordb = vectordb

#     def retrieve(self, query: Any):
#         raise NotImplementedError()

#     def get_langchain_retriever(self):
#         return self.vectordb.get_langchain_client().as_retriever()

#     def get_langchain_memory_retriever(self):
#         return self.vectordb.get_langchain_memory_client().as_retriever()

#     @classmethod
#     def from_config(cls, config):
#         raise NotImplementedError