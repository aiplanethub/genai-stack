from typing import List

from fastapi import APIRouter

from genai_stack.constant import API, VECTORDB
from genai_stack.genai_server.models.vectordb_models import DocumentType, RetrieverAddDocumentsRequestModel, \
    RetrieverAddDocumentsResponseModel, RetrieverSearchRequestModel, RetrieverSearchResponseModel
from genai_stack.genai_server.services.vectordb_service import VectorDBService
from genai_stack.genai_server.settings.settings import settings

service = VectorDBService(store=settings.STORE)

router = APIRouter(
    prefix=API + VECTORDB,
    tags=['vectordb']
)


@router.post("/add-documents")
def add_documents(data: RetrieverAddDocumentsRequestModel) -> RetrieverAddDocumentsResponseModel:
    return service.add_documents(data=data)


@router.get("/search")
def search(data: RetrieverSearchRequestModel) -> RetrieverSearchResponseModel:
    return service.search(data=data)

