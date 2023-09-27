from sqlalchemy.orm import Session
from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.vectordb_models import (
    DocumentType, RetrieverAddDocumentsRequestModel, RetrieverSearchRequestModel, RetrieverAddDocumentsResponseModel,
    RetrieverSearchResponseModel
)
from genai_stack.genai_server.schemas import StackSessionSchema
from genai_stack.genai_server.utils import get_current_stack
from genai_stack.genai_server.settings.config import stack_config


class VectorDBService(BaseService):

    def add_documents(self, data: RetrieverAddDocumentsRequestModel) -> RetrieverAddDocumentsResponseModel:

        with Session(self.engine) as session:
            stack_session = session.get(StackSessionSchema, data.session_id)
            stack = get_current_stack(config=stack_config, session=stack_session)
            stack.vectordb.add_documents(data.documents)
            return RetrieverAddDocumentsResponseModel(documents=[
                DocumentType(
                    page_content=document.page_content,
                    metadata=document.metadata
                ) for document in data.documents
            ])

    def search(self, data: RetrieverSearchRequestModel) -> RetrieverSearchResponseModel:

        with Session(self.engine) as session:
            stack_session = session.get(StackSessionSchema, data.session_id)
            stack = get_current_stack(config=stack_config, session=stack_session)
            documents = stack.vectordb.search(data.query)
            return RetrieverSearchResponseModel(documents=[
                DocumentType(
                    page_content=document.page_content,
                    metadata=document.metadata
                ) for document in documents
            ])
