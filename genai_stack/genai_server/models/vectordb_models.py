from typing import List

from pydantic import BaseModel


class DocumentType(BaseModel):
    page_content: str
    metadata: dict


class RetrieverBaseModel(BaseModel):
    session_id: int


class RetrieverAddDocumentsRequestModel(RetrieverBaseModel):
    documents: List[DocumentType]


class RetrieverSearchRequestModel(RetrieverBaseModel):
    query: str


class RetrieverAddDocumentsResponseModel(RetrieverBaseModel):
    documents: List[DocumentType]


class RetrieverSearchResponseModel(RetrieverBaseModel):
    documents: List[DocumentType]
