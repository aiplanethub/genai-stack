from sqlalchemy.orm import Session

from genai_stack.genai_server.schemas.components import ETLJob
from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.etl_models import ETLJobRequestType, ETLJobResponseType
from genai_stack.genai_server.utils import get_current_stack
from genai_stack.genai_server.utils.components import ETLUtil, get_etl_platform
from genai_stack.genai_server.settings.config import stack_config


class ETLService(BaseService):
    def submit_job(self, data: ETLJobRequestType, session) -> ETLJobResponseType:
        stack = get_current_stack(config=stack_config)
        with Session(self.engine) as session:
            etl_job = ETLJob(stack_session=session)
            session.add(etl_job)
            session.commit()

            data = ETLUtil(data).save_request(etl_job.id)

            get_etl_platform(stack=stack).handle_job(**data)

            etl_job.data = data
            session.commit()

        return ETLJobResponseType(
            uuid=etl_job.id,
            session_id=etl_job.stack_session,
            status=etl_job.status,
            metadata=etl_job.metadata,
        )
