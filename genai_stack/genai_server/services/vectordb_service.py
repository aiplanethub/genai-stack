from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.vectordb_models import (
    DocumentType, RetrieverAddDocumentsRequestModel, RetrieverSearchRequestModel, RetrieverAddDocumentsResponseModel,
    RetrieverSearchResponseModel
)
from genai_stack.genai_server.utils import get_current_stack
from genai_stack.genai_server.settings.config import stack_config


class VectorDBService(BaseService):

    def add_documents(self, data: RetrieverAddDocumentsRequestModel) -> RetrieverAddDocumentsResponseModel:
        """
        This method adds the documents to the vector database.

            Args
                session_id : int
                documents : List[DocumentType]

            Returns
                bool
        """
        stack = get_current_stack(config=stack_config)
        stack.vector_db.add_documents(data.documents)
        return RetrieverAddDocumentsResponseModel(documents=[
            DocumentType(
                page_content=document['page_content'],
                metadata=document['metadata']
            ) for document in data.documents
        ])

    def search(self, data: RetrieverSearchRequestModel) -> RetrieverSearchResponseModel:
        """
        This method searches the documents from the vector database.

            Args
                session_id : int
                query : str

            Returns
                documents : List[DocumentType]
        """
        stack = get_current_stack(config=stack_config)
        documents = stack.vector_db.search(data.query)
        return RetrieverSearchResponseModel(documents=[
            DocumentType(
                page_content=document['page_content'],
                metadata=document['metadata']
            ) for document in documents
        ])
