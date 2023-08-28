import typing
from pydantic import BaseModel

from genai_stack.stack.stack_component import StackComponent, StackComponentConfig


class BaseEmbeddingConfigModel(BaseModel):
    """
    Data Model for the configs
    """

    pass


class BaseEmbeddingConfig(StackComponentConfig):
    data_model = BaseEmbeddingConfigModel


class BaseEmbedding(StackComponent):
    config_class = BaseEmbeddingConfig

    def load(self):
        """
        Load the embedding
        """
        raise NotImplementedError()

    def embed_text(self, text: str):
        """
        Embed the text and return the embedding

        Args:
            text: Text to embed

        Returns:
            Embedded vector
        """
        raise NotImplementedError()
