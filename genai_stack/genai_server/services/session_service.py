from fastapi import HTTPException
from typing import List, Union
from sqlalchemy.orm import Session
import importlib
from genai_stack.embedding.langchain import LangchainEmbedding

from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.session_models import (
    StackSessionRequestModel,
    StackSessionResponseModel,
    StackSessionFilterModel
)
from genai_stack.genai_store.schemas.session_schemas import StackSessionSchema
from genai_stack.stack.stack import Stack
from genai_stack.constants import vectordb, memory
from genai_stack.genai_server.settings.config import stack_config
from genai_stack.model.gpt3_5 import OpenAIGpt35Model
from genai_stack.llm_cache.cache import LLMCache


def get_class_path(module:str, maps:str, class_name:str):
    class_path = f"{module}.{maps.get(class_name).replace('/','.')}"
    module_path, class_name = class_path.rsplit(".", 1)
    cls = getattr(importlib.import_module(module_path), class_name)
    return cls


def get_class_name(module_name:str):
    return stack_config.get("components").get(module_name).get("name")


def get_class_config(module_name:str):
    return stack_config.get("components").get(module_name).get("config")

config = {
            "model_name": "sentence-transformers/all-mpnet-base-v2",
            "model_kwargs": {"device": "cpu"},
            "encode_kwargs": {"normalize_embeddings": False},
        }
embedding = LangchainEmbedding.from_kwargs(name="HuggingFaceEmbeddings", fields=config)


class SessionService(BaseService):
    @staticmethod
    def get_current_stack():
        """This method returns a singleton stack with the provided configurations."""

        vectordb_cls = get_class_path(
            vectordb.VECTORDB_MODULE, 
            vectordb.AVAILABLE_VECTORDB_MAPS, 
            get_class_name("vectordb")
        )
        
        memory_cls = get_class_path(
            memory.MEMORY_MODULE, 
            memory.AVAILABLE_MEMORY_MAPS,
            get_class_name("memory")
        )

        stack = Stack(
            model=OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": "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"}),
            vectordb=vectordb_cls.from_kwargs(**get_class_config("vectordb")),
            memory=memory_cls.from_kwargs(**get_class_config("memory")),
            embedding=embedding
        )

        return stack


    def create_session(self) -> StackSessionResponseModel:
        """
        This method create a new session for a stack.

            Args
                stack_id : int
                meta_data : dict
            
            Returns
                id : int
                stack_id : int
                meta_data : dict
                create_at : datetime
                modified_at : None
        """
        stack = self.get_current_stack()


        with Session(self.engine) as session:
            # stack:Union[StackSchema, None] = Session.get(StackSchema, _session.stack_id)        

            # if stack is None:
            #     raise HTTPException(status_code=404, detail=f"Stack with id {_session.stack_id} does not exist.")
            
            # if len(stack.components) == 0:
            #     raise HTTPException(status_code=400, detail=f"Stack with id {stack.id} does not contains component.")
            
            _session = StackSessionSchema(stack_id=1, meta_data = {})

            session.add(_session)
            session.commit()

            created_session = session.get(StackSessionSchema, _session.id)

            normal_index = stack.vectordb.create_index(index_name = f"{created_session.stack_id}-{created_session.id}")
            memory_index = stack.vectordb.create_index(index_name = f"{created_session.stack_id}-{created_session.id}-memory")
            cache_index = stack.vectordb.create_index(index_name = f"{created_session.stack_id}-{created_session.id}-cache")

            created_session.meta_data={
                "indexstore":f"{created_session.stack_id}-{created_session.id}",
                "memory_index":f"{created_session.stack_id}-{created_session.id}-memory",
                "cache_index":f"{created_session.stack_id}-{created_session.id}-cache"
            }

            session.commit()
            
            return StackSessionResponseModel(
                id=_session.id,
                stack_id=_session.stack_id,
                meta_data=_session.meta_data,
                created_at=_session.created_at,
                modified_at=_session.modified_at
            )
    
    def sessions_list(self) -> Union[List[StackSessionResponseModel], List]:
        """This method returns the sessions list."""

        with Session(self.engine) as session:
            sessions = session.query(StackSessionSchema).all()

            return sessions
        
    def get_session(self, filter:StackSessionFilterModel) -> StackSessionResponseModel:
        """This method returns the existing session."""

        with Session(self.engine) as session:
            old_session = session.get(StackSessionSchema, filter.id)

            if old_session is None:
                raise HTTPException(status_code=404, detail=f"Session with id {filter.id} doest not exist.")
            
            return StackSessionResponseModel(
                id=old_session.id,
                stack_id=old_session.stack_id,
                meta_data=old_session.meta_data,
                created_at=old_session.created_at,
                modified_at=old_session.modified_at
            )
    
    def delete_session(self, filter:StackSessionFilterModel) -> dict:
        """This method deletes the existing session."""

        with Session(self.engine) as session:
            old_session = session.get(StackSessionSchema, filter.id)

            if old_session is None:
                raise HTTPException(status_code=404, detail=f"Session with id {filter.id} doest not exist.")
            
            session.delete(old_session)
            session.commit()

            return {"detail":f"Successfully deleted session {old_session.id}."}