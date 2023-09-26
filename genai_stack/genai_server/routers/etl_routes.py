from fastapi import APIRouter

from genai_stack.constant import API, ETL
from genai_stack.genai_server.database import initialize_store
from genai_stack.genai_server.models.etl_models import ETLJobRequestType, ETLJobResponseType
from genai_stack.genai_server.services.etl_service import ETLService

store = initialize_store()

service = ETLService(store=store)

router = APIRouter(
    prefix=API + ETL,
    tags=['retriever']
)


@router.get("/submit-job")
def extract(data: ETLJobRequestType) -> ETLJobResponseType:
    return service.submit_job(data=data)
