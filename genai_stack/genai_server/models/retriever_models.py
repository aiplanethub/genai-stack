from pydantic import BaseModel


class RetrieverBaseModel(BaseModel):
    pass


class RetrieverRequestModel(RetrieverBaseModel):
    session_id: int
    stack_id: int
    query: str


class RetrieverResponseModel(RetrieverBaseModel):
    output: str
