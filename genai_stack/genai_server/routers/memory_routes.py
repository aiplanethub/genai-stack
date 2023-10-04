from fastapi.routing import APIRouter

from genai_stack.constant import API, MEMORY
from genai_stack.genai_server.models.memory import (
    MemoryAddTextRequestModel,
    MemoryBaseModel,
    MemoryHistoryResponseModel,
    MemoryLatestMessageResponseModel,
)
from genai_stack.genai_server.services.memory import MemoryService
from genai_stack.genai_server.settings.settings import settings

service = MemoryService(store=settings.STORE)

router = APIRouter(prefix=API + MEMORY, tags=["memory"])


@router.post("/add-text", response_model=MemoryLatestMessageResponseModel)
def add_texts_to_memory(data: MemoryAddTextRequestModel):
    return service.add_to_memory(data=data)


@router.post("/get-latest-text", response_model=MemoryLatestMessageResponseModel)
def get_latest_text_from_memory(data: MemoryBaseModel):
    return service.get_latest_message_from_memory(data=data)


@router.post("/get-history", response_model=MemoryHistoryResponseModel)
def get_history_from_memory(data: MemoryBaseModel):
    return service.get_latest_message_from_memory(data=data)
