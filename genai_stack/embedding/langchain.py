from typing import Optional, Dict, Any

from genai_stack.utils.importing import import_class
from .base import BaseEmbedding, BaseEmbeddingConfig, BaseEmbeddingConfigModel


class LangchainEmbeddingConfigModel(BaseEmbeddingConfigModel):
    name: str
    fields: dict


class LangchainEmbeddingConfig(BaseEmbeddingConfig):
    data_model = LangchainEmbeddingConfigModel


class LangchainEmbedding(BaseEmbedding):
    config_class = LangchainEmbeddingConfig

    def load(self) -> Any:
        embedding_cls = import_class(
            f"langchain.embeddings.{self.config.name}",
        )
        embedding = embedding_cls(**self.config.fields)
        return embedding

    def embed_text(self, text: str):
        return self.embedding.embed_query(text)
