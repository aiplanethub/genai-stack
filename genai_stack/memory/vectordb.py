from typing import Optional
from genai_stack.memory.base import BaseMemory, BaseMemoryConfig, BaseMemoryConfigModel
from genai_stack.memory.utils import (
    create_kwarg_map
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
        self.mediator.add_chat_conversation(
            user_text=user_text,
            model_text=model_text,
            kwarg_map=self.kwarg_map
        )

    def get_chat_history(self):
        return self.mediator.get_vectordb_chat_history(
            kwarg_map=self.kwarg_map, 
            k=self.config.k
        )