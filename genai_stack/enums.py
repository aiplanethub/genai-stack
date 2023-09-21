import logging
from enum import Enum


class LoggingLevels(Enum):
    """Enum for logging levels."""

    NOTSET = logging.NOTSET
    ERROR = logging.ERROR
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    CRITICAL = logging.CRITICAL


class StackComponentType(Enum):
    """All possible types a `StackComponent` can have."""

    ETL = "etl"
    EMBEDDING = "embedding"
    VECTOR_DB = "vector_db"
    MODEL = "model"
    PROMPT_ENGINE = "prompt_engine"
    RETRIEVER = "retriever"
    MEMORY = "memory"

class Actions(str, Enum):
    GET = "get",
    CREATE = "create"
