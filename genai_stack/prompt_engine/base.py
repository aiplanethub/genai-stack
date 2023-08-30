from typing import Union

from genai_stack.model import BaseModel
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

    def validate_prompt(self, prompt: str) -> Union[bool, None]:
        """
        This method validates the prompt
        """
        raise NotImplementedError()
