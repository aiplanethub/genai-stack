from typing import Optional, Dict
from langchain.llms import HuggingFacePipeline

from genai_stack.model.base import BaseModel, BaseModelConfig, BaseModelConfigModel


class HuggingFaceModelConfigModel(BaseModelConfigModel):
    """
    Data Model for the configs
    """

    model: Optional[str] = "nomic-ai/gpt4all-j"
    """Model name to use."""
    model_kwargs: Optional[Dict] = None
    """Key word arguments passed to the model."""
    pipeline_kwargs: Optional[dict] = None
    """Key word arguments passed to the pipeline."""
    task: str = "text-generation"
    """Valid tasks: 'text2text-generation', 'text-generation', 'summarization'"""


class HuggingFaceModelConfig(BaseModelConfig):
    data_model = HuggingFaceModelConfigModel


class HuggingFaceModel(BaseModel):
    config_class = HuggingFaceModelConfig

    def _post_init(self, *args, **kwargs):
        self.model = self.load()

    def load(self):
        model = HuggingFacePipeline.from_model_id(
            model_id=self.config.model, task=self.config.task, model_kwargs=self.config.model_kwargs
        )
        return model

    def predict(self, prompt: str):
        response = self.model(prompt)
        # Note: Huggingface model response format is different for different model
        # so user should extract the info which is required.
        return {"output": response}
