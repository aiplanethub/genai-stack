from pydantic import BaseModel

from genai_stack.stack.stack_component import StackComponent
from genai_stack.stack.stack_component_config import StackComponentConfig


class BaseLLMCacheConfigModel(BaseModel):
    """
    Data Model for the configs
    """

    pass


class BaseLLMCacheConfig(StackComponentConfig):
    data_model = BaseLLMCacheConfigModel


class BaseLLMCache(StackComponent):

    def get_cache(self, query: str, metadata: dict):
        raise NotImplementedError

    def set_cache(self, query: str, response: str, metadata: dict):
        raise NotImplementedError
