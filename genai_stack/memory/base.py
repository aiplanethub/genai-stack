from pydantic import BaseModel
from genai_stack.stack.stack_component import StackComponentConfig, StackComponent

class BaseMemoryConfigModel(BaseModel):
    """
    Data Model for the configs
    """
    pass


class BaseMemoryConfig(StackComponentConfig):
    data_model = BaseMemoryConfigModel


class BaseMemory(StackComponent):
    
    def get_user_text(self) -> str:
        """
        This method returns the user query
        """
        raise NotImplementedError()

    def get_model_text(self) -> str:
        """
        This method returns the model response
        """
        raise NotImplementedError()
    
    def get_text(self) -> dict:
        """
        This method returns both user query and model response
        """
        raise NotImplementedError()
    
    def add_text(self, user_text:str, model_text:str) -> None:
        """
        This method stores both user query and model response
        """
        raise NotImplementedError()
    
    def get_chat_history(self) -> str:
        """
        This method returns the chat conversation history
        """
        raise NotImplementedError()