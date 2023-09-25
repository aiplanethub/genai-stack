from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.retriever_models import RetrieverResponseModel, RetrieverRequestModel
from genai_stack.genai_server.utils import get_current_stack
from genai_stack.genai_server.settings.config import stack_config


class RetrieverService(BaseService):

    def retrieve(self, request: RetrieverRequestModel) -> RetrieverResponseModel:
        """
        This method retrieves the documents from the vector database.

            Args
                session_id : int
                query : str

            Returns
                documents : List[DocumentType]
        """
        stack = get_current_stack(config=stack_config)
        response = stack.retriever.retrieve(request.query)
        return RetrieverResponseModel(
            output=response['output']
        )
