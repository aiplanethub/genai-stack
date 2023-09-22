from typing import List

from fastapi import APIRouter

from genai_stack.constant import API, VECTORDB
from genai_stack.genai_platform.database import initialize_store
from genai_stack.genai_server.models.vectordb_models import DocumentType
from genai_stack.genai_server.services.vectordb_service import VectorDBService

store = initialize_store()

service = VectorDBService(store=store)

router = APIRouter(
    prefix=API + VECTORDB,
    tags=['vectordb']
)


@router.get("/add-documents/{session_id}")
def add_documents(session_id: int, documents: List[DocumentType]) -> bool:
    return service.add_documents(session_id=session_id, documents=documents)


@router.get("/search/{session_id}")
def search(session_id: int, query: str) -> List[DocumentType]:
    return service.search(session_id=session_id, query=query)

