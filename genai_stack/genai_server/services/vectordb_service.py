from typing import List

from sqlalchemy.orm import Session

from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.vectordb_models import DocumentType
from genai_stack.genai_server.utils import get_current_stack
from genai_stack.vectordb.weaviate_db import Weaviate
from genai_stack.vectordb.chromadb import ChromaDB


class VectorDBService(BaseService):

    def add_documents(self, documents: List[DocumentType]) -> List[DocumentType]:
        """
        This method adds the documents to the vector database.

            Args
                session_id : int
                documents : List[DocumentType]

            Returns
                bool
        """
        stack = get_current_stack()
        stack.vector_db.add_documents(documents)
        return [
            DocumentType(
                page_content=document['page_content'],
                metadata=document['metadata']
            ) for document in documents
        ]

    def search(self, query: str) -> List[DocumentType]:
        """
        This method searches the documents from the vector database.

            Args
                session_id : int
                query : str

            Returns
                documents : List[DocumentType]
        """
        stack = get_current_stack()
        documents = stack.vector_db.search(query)
        return [
            DocumentType(
                page_content=document['page_content'],
                metadata=document['metadata']
            ) for document in documents
        ]
