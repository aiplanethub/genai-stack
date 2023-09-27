from sqlalchemy.orm import Session

from genai_stack.genai_server.schemas.components import ETLJob
from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.etl_models import ETLJobRequestType, ETLJobResponseType
from genai_stack.genai_server.utils import get_current_stack
from genai_stack.genai_server.settings.config import stack_config


class ETLService(BaseService):
    def submit_job(self, data: ETLJobRequestType, session) -> ETLJobResponseType:
        stack = get_current_stack(config=stack_config)
        with Session(self.engine) as session:
            etl_job = ETLJob(stack_session = session)
            session.add(etl_job)
            session.commit()

            

        return ETLJobResponseType(
            uuid=response["uuid"],
            session_id=response["session_id"],
            status=response["status"],
            metadata=response["metadata"],
        )
