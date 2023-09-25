import json
from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.retriever_models import RetrieverResponseModel, RetrieverRequestModel
from genai_stack.genai_server.utils import get_current_stack


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
        file = open("genai_stack/genai_server/config.json", "r")
        config = json.loads(file.read())
        file.close()
        stack = get_current_stack(
            stack_id=request.stack_id,
            session_id=request.session_id,
            session_indexes={},
            config=config
        )
        response = stack.retriever.retrieve(request.query)
        return RetrieverResponseModel(
            output=response['output']
        )
