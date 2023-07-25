from .base import BaseModel

from typing import Optional, Any
from langchain.llms.openai import OpenAI


class OpenAIModel:
    vector_store: Optional[Any] = None

    def load(self, model_path: str):
        self.model_path = model_path

    def predict(self, query: Any):
        pass
