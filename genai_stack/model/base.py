from typing import Any
from pydantic import BaseModel as PydanticBaseModel

from genai_stack.stack.stack_component import StackComponent, StackComponentConfig


class BaseModelConfigModel(PydanticBaseModel):
    """
    Data Model for the configs
    """

    pass


class BaseModelConfig(StackComponentConfig):
    data_model = BaseModelConfigModel


class BaseModel(StackComponent):
    config_class = BaseModelConfig

    def _post_init(self, *args, **kwargs):
        self.model = self.load()

    def load(self):
        raise NotImplementedError

    def predict(self, query: Any):
        raise NotImplementedError

    def parameters(self):
        pass
