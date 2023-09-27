from enum import Enum


class StackComponentType(str, Enum):
    """All possible types a `StackComponent` can have."""

    ETL = "etl"
    EMBEDDING = "embedding"
    VECTOR_DB = "vectordb"
    MODEL = "model"
    PROMPT_ENGINE = "prompt_engine"
    RETRIEVER = "retriever"
    MEMORY = "memory"
    CACHE = "llm_cache"


class Actions(str, Enum):
    GET = ("get",)
    CREATE = "create"
