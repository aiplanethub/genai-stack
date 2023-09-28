from fastapi import APIRouter, Request
from typing import Any

from genai_stack.constant import API, ETL
from genai_stack.genai_server.settings.settings import settings
from genai_stack.genai_server.models.etl_models import ETLJobRequestType, ETLJobResponseType
from genai_stack.genai_server.services.etl_service import ETLService

service = ETLService(store=settings.STORE)

router = APIRouter(prefix=API + ETL, tags=["etl"])


@router.post("/submit-job", response_model=ETLJobResponseType)
async def extract(request: Request, session_id: int = None) -> Any:
    request_body = await request.form()
    return service.submit_job(data=request_body, stack_session_id=session_id)
