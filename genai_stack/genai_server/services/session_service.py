from fastapi import HTTPException
from typing import List, Union
from sqlalchemy.orm import Session

from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.session_models import (
    StackSessionResponseModel,
    StackSessionFilterModel
)
from genai_stack.genai_server.utils import generate_index_names, get_current_stack
from genai_stack.genai_store.schemas.session_schemas import StackSessionSchema
from genai_stack.genai_server.settings.config import stack_config


class SessionService(BaseService):

    def create_session(self, session_indexes) -> StackSessionResponseModel:
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
        stack = get_current_stack(stack_config)

        with Session(self.engine) as session:

            _session = StackSessionSchema(stack_id=1, meta_data={})

            session.add(_session)
            session.commit()

            index_names = generate_index_names(
                stack_id=_session.stack_id,
                session_id=_session.id,
                session_indexes=session_indexes
            )

            created_session = session.get(StackSessionSchema, _session.id)

            for names in index_names:
                stack.vectordb.create_index(
                    index_name=index_names.get(names)
                )
            created_session.meta_data = index_names
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

    def get_session(self, filter: StackSessionFilterModel) -> StackSessionResponseModel:
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

    def delete_session(self, filter: StackSessionFilterModel) -> dict:
        """This method deletes the existing session."""

        with Session(self.engine) as session:
            old_session = session.get(StackSessionSchema, filter.id)

            if old_session is None:
                raise HTTPException(status_code=404, detail=f"Session with id {filter.id} doest not exist.")

            session.delete(old_session)
            session.commit()

            return {"detail": f"Successfully deleted session {old_session.id}."}
