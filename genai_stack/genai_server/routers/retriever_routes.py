from fastapi import APIRouter

from genai_stack.constant import API, RETRIEVER
from genai_stack.genai_platform.database import initialize_store
from genai_stack.genai_server.models.retriever_models import RetrieverResponseModel, RetrieverRequestModel
from genai_stack.genai_server.services.retriever_service import RetrieverService

store = initialize_store()

service = RetrieverService(store=store)

router = APIRouter(
    prefix=API + RETRIEVER,
    tags=['retriever']
)


@router.get("/retrieve/{session_id}")
def retrieve(session_id: int, retriever: RetrieverRequestModel) -> RetrieverResponseModel:
    return service.retrieve(session_id=session_id, query=retriever.query)

