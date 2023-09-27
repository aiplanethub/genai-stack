from pydantic import BaseModel


class RetrieverBaseModel(BaseModel):
    session_id: int


class RetrieverRequestModel(RetrieverBaseModel):
    query: str


class RetrieverResponseModel(RetrieverBaseModel):
    output: str
