

MEMORY_MODULE = "genai_stack.memory"
MEMORY_CONFIG_KEY = "memory"


class Memory:
    CONVERSATION_BUFFER = "conversation_buffer"
    WEAVIATE = "weaviate"
    CHROMADB = "chromadb"


AVAILABLE_MEMORY_MAPS = {
    Memory.CONVERSATION_BUFFER:"langchain/ConversationBufferMemory",
    Memory.WEAVIATE: "weaviate/Weaviate", 
    Memory.CHROMADB: "chromadb/ChromaDB"
}
