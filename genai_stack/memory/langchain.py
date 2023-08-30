from langchain.memory import ConversationBufferMemory as cbm
from .base import BaseMemory

class ConversationBufferMemory(BaseMemory):
    memory = None
    input_text = None
    output_text = None

    def _post_init(self, *args, **kwargs):
        self.memory = cbm(return_messages=True)

    def add_text(self, user_text, model_text):
        self.input_text = user_text
        self.output_text = model_text
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
