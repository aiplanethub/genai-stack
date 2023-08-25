from typing import Dict
from .base import BaseResponseEvaluatorConfigModel, BaseResponseEvaluatorConfig, BaseResponseEvaluator

class GuardRailsConfigModel(BaseResponseEvaluatorConfigModel):
    prompt:str
    output_format:Dict
    model_name:str
    max_token:int
    temperature:float


class GuardRailsConfig(BaseResponseEvaluatorConfig):
    data_model = GuardRailsConfigModel

class GuardRails(BaseResponseEvaluator):
    config_class = GuardRailsConfig

    @classmethod
    def config_class() -> GuardRailsConfig:
        return GuardRailsConfig
    

