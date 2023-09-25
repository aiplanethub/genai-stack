MEMORY_MODULE = "genai_stack.memory"
MEMORY_CONFIG_KEY = "memory"


class Memory:
    LANGCHAIN = "langchain"


AVAILABLE_MEMORY_MAPS = {
    Memory.LANGCHAIN:"langchain/ConversationBufferMemory",
}
