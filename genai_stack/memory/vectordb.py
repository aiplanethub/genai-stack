from typing import Optional
from genai_stack.memory.base import BaseMemory, BaseMemoryConfig, BaseMemoryConfigModel
from genai_stack.memory.utils import (
    create_kwarg_map,
    format_conversation,
    get_conversation_from_document,
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
        id = "7a476819-799d-4f0b-a57a-300cc10d130f"

        _kwarg_map = {**self.kwarg_map}

        # Storing a random embeddings
        _kwarg_map['ChromaDB']['embeddings'] = [1,2,3,4]

        document = self.mediator.get_document(id=id, kwarg_map=_kwarg_map)
        
        if not document:
            conversation = format_conversation(user_text=user_text, model_text=model_text)
            self.mediator.create_document(id=id, document=conversation, kwarg_map=_kwarg_map)
        else:
            old_conversation = get_conversation_from_document(
                document=document, 
                kwarg_map=_kwarg_map
            )
            conversation = format_conversation(
                user_text=user_text, 
                model_text=model_text, 
                append=True, 
                old_conversation=old_conversation
            )
            self.mediator.update_document(
                id=id, 
                document=conversation, 
                kwarg_map=_kwarg_map
            )

    def get_chat_history(self):
        id = "7a476819-799d-4f0b-a57a-300cc10d130f"

        document = self.mediator.get_document(id=id, kwarg_map=self.kwarg_map)

        if not document:
            return "No conversations available."
        else:
            conversation = get_conversation_from_document(
                document=document, 
                kwarg_map=self.kwarg_map
            )
            conversations = conversation.split("\n\n")
            return parse_vectordb_chat_conversations(search_results=conversations)