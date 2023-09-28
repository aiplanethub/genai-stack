from fastapi import APIRouter

from genai_stack.constant import API, ETL
from genai_stack.genai_server.settings.settings import settings
from genai_stack.genai_server.models.etl_models import ETLJobRequestType, ETLJobResponseType
from genai_stack.genai_server.services.etl_service import ETLService

service = ETLService(store=settings.STORE)

router = APIRouter(prefix=API + ETL, tags=["etl"])


@router.get("/submit-job")
def extract(data: ETLJobRequestType, session_id: int = None) -> ETLJobResponseType:
    return service.submit_job(data=data, session_id=session_id)
