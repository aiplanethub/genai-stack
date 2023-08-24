from typing import Optional, Dict

from langchain.embeddings import HuggingFaceEmbeddings

from .base import BaseEmbedding, BaseEmbeddingConfig, BaseEmbeddingConfigModel


class HuggingFaceEmbeddingConfigModel(BaseEmbeddingConfigModel):
    model_name: str
    model_kwargs: Dict
    encode_kwargs: Optional[Dict]


class HuggingFaceEmbeddingConfig(BaseEmbeddingConfig):
    data_model = HuggingFaceEmbeddingConfigModel


class HuggingFaceEmbedding(BaseEmbedding):
    config_class = HuggingFaceEmbeddingConfig

    def load(self) -> HuggingFaceEmbeddings:
        return HuggingFaceEmbeddings(
            model_name=self.config.model_name,
            model_kwargs=self.config.model_kwargs,
            encode_kwargs=self.config.encode_kwargs,
        )

    def embed_text(self, text: str):
        return self.embedding.embed_query(text)
