from langchain.memory import ConversationBufferMemory as cbm
from .base import BaseMemoryConfigModel, BaseMemoryConfig, BaseMemory


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
        return self.input_text
    
    def get_model_text(self):
        return self.output_text
    
    def get_text(self):
        return {
            "user_text":self.get_user_text(), 
            "model_text":self.get_model_text()
        }

    def get_chat_history(self):
        return self.memory.load_memory_variables({})
    


obj = ConversationBufferMemory()
print(obj)
