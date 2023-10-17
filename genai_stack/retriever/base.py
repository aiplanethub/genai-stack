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

    def get_prompt(self, query: str):
        """
        This method returns the prompt template from the prompt engine component
        """
        return self.mediator.get_prompt_template(query)

    def retrieve(self, query: str) -> dict:
        """
        This method returns the model response for the prompt template.
        """
        raise NotImplementedError()

    def get_context(self, query: str):
        """
        This method returns the relevant documents returned by the similarity search from a vectordb based on the query
        """
        raise NotImplementedError()

    def get_chat_history(self) -> str:
        """
        This method returns the chat conversation history
        """
        return self.mediator.get_chat_history()
