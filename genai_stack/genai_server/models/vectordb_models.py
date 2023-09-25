from typing import List

from pydantic import BaseModel


class DocumentType(BaseModel):
    page_content: str
    metadata: dict


class RetrieverBaseRequestModel(BaseModel):
    session_id: int
    stack_id: int


class RetrieverAddDocumentsRequestModel(RetrieverBaseRequestModel):
    documents: List[DocumentType]


class RetrieverSearchRequestModel(RetrieverBaseRequestModel):
    query: str


class RetrieverBaseResponseModel(BaseModel):
    pass


class RetrieverAddDocumentsResponseModel(RetrieverBaseResponseModel):
    documents: List[DocumentType]


class RetrieverSearchResponseModel(RetrieverBaseResponseModel):
    documents: List[DocumentType]
