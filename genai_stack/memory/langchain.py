from langchain.memory import ConversationBufferMemory as cbm
from genai_stack.memory.base import BaseMemoryConfigModel, BaseMemoryConfig, BaseMemory
from genai_stack.memory.utils import parse_chat_conversation_history


class ConversationBufferMemoryConfigModel(BaseMemoryConfigModel):
    """
    Data Model for the configs
    """
    pass


class ConversationBufferMemoryConfig(BaseMemoryConfig):
    data_model = ConversationBufferMemoryConfigModel


class ConversationBufferMemory(BaseMemory):
    config_class = ConversationBufferMemoryConfig
    memory = None

    def _post_init(self, *args, **kwargs):
        self.memory = cbm(return_messages=True)

    def add_text(self, user_text, model_text):
        self.memory.save_context({"input": user_text}, {"output": model_text})

    def get_user_text(self):
        if len(self.memory.chat_memory.messages) == 0:
            return None
        return self.memory.chat_memory.messages[-2].content
    
    def get_model_text(self):
        if len(self.memory.chat_memory.messages) == 0:
            return None
        return self.memory.chat_memory.messages[-1].content
    
    def get_text(self):
        return {
            "user_text":self.get_user_text(), 
            "model_text":self.get_model_text()
        }

    def get_chat_history(self):
        return parse_chat_conversation_history(self.memory.chat_memory.messages)