from typing import Optional, Union, Any, Dict, Tuple
from pydantic import Field
from langchain.chat_models import AzureChatOpenAI

from genai_stack.model.base import BaseModel, BaseModelConfig, BaseModelConfigModel

class AzureModelParameters(BaseModelConfigModel):
    model_name: str = Field(default="gpt-4", alias="model")
    azure_deployment: str 
    temperature: float = 0.1
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    api_key: str
    openai_api_version: str = Field(default="2024-02-01",alias="api_version")
    streaming: bool = False
    azure_endpoint: str

    
class AzureModelConfigModel(BaseModelConfigModel):
    """
    Data Model for the configs
    """

    parameters: AzureModelParameters

class AzureModelConfig(BaseModelConfig):
    data_model = AzureModelConfigModel

class AzureModel(BaseModel):
    config_class = AzureModelConfig

    def _post_init(self, *args, **kwargs):
        self.model = self.load()

    def load(self):
        """
        Using dict method here to dynamically access object attributes
        """
        model = AzureChatOpenAI(**self.config.parameters.dict())
        return model

    def predict(self, prompt: str):
        response = self.model.predict(prompt)
        return {"output": response}
