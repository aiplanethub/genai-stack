EMBEDDING_MODULE = "genai_stack.embedding"
EMBEDDING_CONFIG_KEY = "embedding"


class EMBEDDING:
    LANGCHAIN = "langchain"


AVAILABLE_EMBEDDING_MAPS = {
    EMBEDDING.LANGCHAIN:"langchain/LangchainEmbedding",
}
