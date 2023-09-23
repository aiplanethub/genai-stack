from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.retriver_models import RetrieverResponseModel
from genai_stack.genai_server.utils import get_current_stack


class RetrieverService(BaseService):

    def retrieve(self, query: str, session_id: int) -> RetrieverResponseModel:
        """
        This method retrieves the documents from the vector database.

            Args
                session_id : int
                query : str

            Returns
                documents : List[DocumentType]
        """
        stack = get_current_stack()
        response = stack.retriever.retrieve(query)
        return RetrieverResponseModel(
            output=response['output']
        )
