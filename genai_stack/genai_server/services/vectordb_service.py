from typing import List

from sqlalchemy.orm import Session

from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.vectordb_models import DocumentType
from genai_stack.vectordb.weaviate_db import Weaviate
from genai_stack.vectordb.chromadb import ChromaDB


class VectorDBService(BaseService):

    def add_documents(self, session_id: int, documents: List[DocumentType]) -> List[DocumentType]:
        """
        This method adds the documents to the vector database.

            Args
                session_id : int
                documents : List[DocumentType]

            Returns
                bool
        """
        with Session(self.engine) as session:

            if config['type'] == 'chroma':
                vector_db = ChromaDB.from_kwargs(**config)
            else:
                vector_db = Weaviate.from_kwargs(**config)
            vector_db.add_documents(documents)
            return [
                DocumentType(
                    page_content=document['page_content'],
                    metadata=document['metadata']
                ) for document in documents
            ]

    def search(self, session_id: int, query: str) -> List[DocumentType]:
        """
        This method searches the documents from the vector database.

            Args
                session_id : int
                query : str

            Returns
                documents : List[DocumentType]
        """
        config = {}  # logic for configuration
        if config['type'] == 'chroma':
            vector_db = ChromaDB.from_kwargs(**config)
        else:
            vector_db = Weaviate.from_kwargs(**config)
        documents = vector_db.search(query)
        return [
            DocumentType(
                page_content=document['page_content'],
                metadata=document['metadata']
            ) for document in documents
        ]
