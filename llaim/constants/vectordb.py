from enum import Enum
from vectordb import Weaviate


class VectorDB:
    WEAVIATE = "weaviate"


VECTOR_DB_CLIENT_MAP = {VectorDB.WEAVIATE: Weaviate}

RETRIEVAL_CONFIG_VECTORDB = "vectordb"
