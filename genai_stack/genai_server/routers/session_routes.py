from fastapi import APIRouter
from typing import List, Union

from genai_stack.constant import API, SESSION
from genai_stack.genai_server.services.session_service import SessionService
from genai_stack.genai_server.models.session_models import StackSessionRequestModel, StackSessionResponseModel, \
    StackSessionFilterModel
from genai_stack.genai_server.database import initialize_store

store = initialize_store()

service = SessionService(store=store)

router = APIRouter(
    prefix=API + SESSION,
    tags=['session']
)


@router.post("")
def create_session(session:StackSessionRequestModel) -> StackSessionResponseModel:
    return service.create_session(session)


@router.get("")
def sessions_list() -> Union[List[StackSessionResponseModel], List]:
    return service.sessions_list()


@router.get("/{session_id}")
def get_session(session_id: int) -> StackSessionResponseModel:
    filter = StackSessionFilterModel(id=session_id)
    return service.get_session(filter)


@router.delete("/{session_id}")
def delete_session(session_id: int) -> dict:
    filter = StackSessionFilterModel(id=session_id)
    return service.delete_session(filter)
