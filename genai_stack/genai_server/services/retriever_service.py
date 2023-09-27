from sqlalchemy.orm import Session

from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.retriever_models import RetrieverResponseModel, RetrieverRequestModel
from genai_stack.genai_server.schemas import StackSessionSchema
from genai_stack.genai_server.utils import get_current_stack
from genai_stack.genai_server.settings.config import stack_config


class RetrieverService(BaseService):

    def retrieve(self, data: RetrieverRequestModel) -> RetrieverResponseModel:
        with Session(self.engine) as session:
            stack_session = session.get(StackSessionSchema, data.session_id)
            stack = get_current_stack(config=stack_config, session=stack_session)
            response = stack.retriever.retrieve(data.query)
            return RetrieverResponseModel(
                output=response['output']
            )
