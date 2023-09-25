from genai_stack.embedding.base import BaseEmbedding

from genai_stack.services.local import LocalService, LocalServiceConfig


class EmbeddingServiceConfig(LocalServiceConfig):
    embedding_component: BaseEmbedding


class EmbeddingService(LocalService):
    config_class = EmbeddingServiceConfig

    def run(self):
        pass