from langchain import PromptTemplate
from pydantic import BaseModel

from genai_stack.prompt_engine.utils import ValidationResponseDict, PromptTypeEnum
from genai_stack.stack.stack_component import StackComponent
from genai_stack.stack.stack_component_config import StackComponentConfig


class BasePromptEngineConfigModel(BaseModel):
    """
    Data Model for the configs
    """

    pass


class BasePromptEngineConfig(StackComponentConfig):
    data_model = BasePromptEngineConfigModel


class BasePromptEngine(StackComponent):

    def find_prompt_template(self):
        """
        This method finds the prompt template
        """
        raise NotImplementedError()

    def get_prompt_template(self, query: str) -> PromptTemplate:
        """
        This method returns the prompt template for the given prompt type and query
        """
        raise NotImplementedError()

    def validate_prompt(self, text: str) -> ValidationResponseDict:
        """
        This method validates the prompt
        """
        raise NotImplementedError()
