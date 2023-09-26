from fastapi import APIRouter

from genai_stack.constant import API, ETL
from genai_stack.genai_server.database import initialize_store
from genai_stack.genai_server.models.etl_models import (
    BaseRequestType, BaseTransformRequestType, BaseTransformResponseType,
    BaseLoadRequestType, BaseLoadResponseType
)
from genai_stack.genai_server.services.etl_service import ETLService

store = initialize_store()

service = ETLService(store=store)

router = APIRouter(
    prefix=API + ETL,
    tags=['retriever']
)


@router.get("/extract")
def extract(data: BaseRequestType) -> BaseRequestType:
    return service.extract()


@router.get("/transform")
def transform(data: BaseTransformRequestType) -> BaseTransformResponseType:
    return service.transform(data=data)


@router.get("/load")
def load(data: BaseLoadRequestType) -> BaseLoadResponseType:
    return service.load(data=data)
