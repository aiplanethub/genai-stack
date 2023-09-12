from typing import Optional, Dict
from langchain.memory import VectorStoreRetrieverMemory
from genai_stack.memory.base import BaseMemory, BaseMemoryConfig, BaseMemoryConfigModel
from genai_stack.memory.utils import parse_chat_conversation_history_search_result, extract_text


class WeaviateConfigModel(BaseMemoryConfigModel):
    """Data Model for the configs"""
    retrieve_parameters:Optional[Dict] = {
        'search_type':'similarity',
        'search_kwargs':{'k':4}
    }
    collection_name:Optional[str] = "Chat_history"
    text_key:Optional[str] = "default_key"


class WeaviateConfig(BaseMemoryConfig):
    data_model = WeaviateConfigModel


class Weaviate(BaseMemory):
    config_class = WeaviateConfig
    memory = None
    lc_client = None

    def _post_init(self, *args, **kwargs):
        config: WeaviateConfigModel = self.config.config_data
        self.lc_client = self.mediator.get_vectordb(
            index_name=config.collection_name.upper(), 
            text_key=config.text_key
        )
        retriever = self.lc_client.as_retriever(
            **{k:v for k,v in config.retrieve_parameters.items()}
        )
        self.memory = VectorStoreRetrieverMemory(
            retriever=retriever,
            memory_key=config.collection_name.upper(), 
            return_docs=True
        )
    
    def add_text(self, user_text: str, model_text: str):
        self.memory.save_context({"input": user_text}, {"output": model_text})

    def get_user_text(self):
        if self._is_chat_conversation_history_available():
            documents = self._get_all_documents()
            return extract_text(key='user', text=documents[-1][self.config.config_data.text_key])
        else:
            return None
    
    def get_model_text(self):
        if self._is_chat_conversation_history_available():
            documents = self._get_all_documents()
            return extract_text(key='model', text=documents[-1][self.config.config_data.text_key])
        else:
            return None
    
    def _is_chat_conversation_history_available(self) -> bool:
        if len(self._get_all_documents()):
            return True
        else:
            return False
    
    def _get_all_documents(self) -> list:
        config = self.config.config_data
        response = self.lc_client._client.query.get(
            class_name=config.collection_name.upper(),
            properties=[config.text_key]
        ).do()
        documents = response.get('data').get('Get').get(config.collection_name.upper())
        return documents
    
    def get_text(self):
        return {
            "user_text":self.get_user_text(), 
            "model_text":self.get_model_text()
        }

    def get_chat_history(self, query):
        documents = self.memory.load_memory_variables({"prompt": query})[self.memory.memory_key.upper()]
        return parse_chat_conversation_history_search_result(search_results=documents)