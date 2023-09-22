from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.retriver_models import RetrieverResponseModel
from genai_stack.retriever import LangChainRetriever


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
        config = {}  # logic for configuration
        retriever = LangChainRetriever.from_kwargs(**config)
        response = retriever.retrieve(query)
        return RetrieverResponseModel(
            output=response['output']
        )
