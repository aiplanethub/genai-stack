from pydantic import BaseModel

from genai_stack.stack.stack_component import StackComponent, StackComponentConfig


class BaseResponseEvaluatorConfigModel(BaseModel):
    """
    Data Model for the config
    """
    pass


class BaseResponseEvaluatorConfig(StackComponentConfig):
    data_model = BaseResponseEvaluatorConfigModel


class BaseResponseEvaluator(StackComponent):
    config_class = BaseResponseEvaluatorConfig,

    @staticmethod
    def config_class() -> BaseResponseEvaluatorConfig:
        return BaseResponseEvaluatorConfig
