from pydantic import BaseModel


class ModelBaseModel(BaseModel):
    pass


class ModelRequestModel(ModelBaseModel):
    prompt: str


class ModelResponseModel(ModelBaseModel):
    output: str
