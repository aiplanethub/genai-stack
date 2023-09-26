from typing import List

from pydantic import BaseModel

from genai_stack.genai_server.models.vectordb_models import DocumentType


class BaseRequestType(BaseModel):
    session_id: int
    stack_id: int


class BaseTransformRequestType(BaseRequestType):
    source_docs: List[DocumentType]


class BaseTransformResponseType(BaseTransformRequestType):
    pass


class BaseLoadRequestType(BaseRequestType):
    documents: List[DocumentType]


class BaseLoadResponseType(BaseLoadRequestType):
    pass

