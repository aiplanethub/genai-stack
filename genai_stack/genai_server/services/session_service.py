from fastapi import HTTPException
from typing import List, Union
from sqlalchemy.orm import Session

from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.session_models import (
    StackSessionRequestModel,
    StackSessionResponseModel,
    StackSessionFilterModel
)
from genai_stack.genai_store.schemas.session_schemas import StackSessionSchema


class SessionService(BaseService):
    pass

    def create_session(self, _session:StackSessionRequestModel) -> StackSessionResponseModel:
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
        
        with Session(self.engine) as session:
            # stack:Union[StackSchema, None] = Session.get(StackSchema, _session.stack_id)        

            # if stack is None:
            #     raise HTTPException(status_code=404, detail=f"Stack with id {_session.stack_id} does not exist.")
            
            # if len(stack.components) == 0:
            #     raise HTTPException(status_code=400, detail=f"Stack with id {stack.id} does not contains component.")
            
            
            new_session = StackSessionSchema(stack_id=_session.stack_id, meta_data=_session.meta_data)

            session.add(new_session)
            session.commit()

            return StackSessionResponseModel(
                id=new_session.id,
                stack_id=new_session.stack_id,
                meta_data=new_session.meta_data,
                created_at=new_session.created_at,
                modified_at=new_session.modified_at
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