import tempfile

VECTORDB_MODULE = "genai_stack.vectordb"
VECTORDB_CONFIG_KEY = "vectordb"


class VectorDB:
    WEAVIATE = "weaviate_db"
    CHROMADB = "chromadb"


AVAILABLE_VECTORDB_MAPS = {VectorDB.WEAVIATE: "weaviate_db/Weaviate", VectorDB.CHROMADB: "chromadb/ChromaDB"}
