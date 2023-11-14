from typing import Optional
from genai_stack.memory.base import BaseMemory, BaseMemoryConfig, BaseMemoryConfigModel
from genai_stack.memory.utils import (
    create_kwarg_map,
    format_conversation,
    parse_vectordb_chat_conversations
)


class VectorDBMemoryConfigModel(BaseMemoryConfigModel):
    """Data Model for the configs"""

    index_name:Optional[str] = 'ChatHistory'
    k:Optional[int] = 4


class VectorDBMemoryConfig(BaseMemoryConfig):
    data_model = VectorDBMemoryConfigModel


class VectorDBMemory(BaseMemory):
    config_class = VectorDBMemoryConfig
    lc_client = None

    def _post_init(self, *args, **kwargs):
        config:VectorDBMemoryConfigModel  = self.config.config_data
        
        self.kwarg_map = create_kwarg_map(config=config)

        self.lc_client = self.mediator.create_index(kwarg_map=self.kwarg_map)

    def add_text(self, user_text: str, model_text: str):
        conversation = format_conversation(user_text=user_text, model_text=model_text)
        self.mediator.create_document(document=conversation, kwarg_map=self.kwarg_map)

    def _get_documents(self):
        return self.mediator.get_documents(kwarg_map=self.kwarg_map)

    def get_chat_history(self):
        documents = self.mediator.get_documents(kwarg_map=self.kwarg_map)
        return parse_vectordb_chat_conversations(
            search_results=documents, 
            k=self.config.config_data.k
        )