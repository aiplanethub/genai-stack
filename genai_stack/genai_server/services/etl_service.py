from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.etl_models import (
    BaseRequestType, BaseTransformRequestType, BaseTransformResponseType,
    BaseLoadRequestType, BaseLoadResponseType
)
from genai_stack.genai_server.utils import get_current_stack
from genai_stack.genai_server.settings.config import stack_config


class ETLService(BaseService):

    def extract(self) -> BaseRequestType:
        stack = get_current_stack(config=stack_config)

        response = stack.etl.extract()

        return BaseRequestType(
            session_id=response['session_id'],
            stack_id=response['stack_id']
        )

    def transform(self,  data: BaseTransformRequestType) -> BaseTransformResponseType:
        stack = get_current_stack(config=stack_config)

        response = stack.etl.transform()

        return BaseTransformResponseType(
            session_id=response['session_id'],
            stack_id=response['stack_id'],
            source_docs=response['source_docs']
        )

    def load(self, data: BaseLoadRequestType) -> BaseLoadResponseType:
        stack = get_current_stack(config=stack_config)

        response = stack.etl.load()

        return BaseLoadResponseType(
            session_id=response['session_id'],
            stack_id=response['stack_id'],
            documents=response['documents']
        )
