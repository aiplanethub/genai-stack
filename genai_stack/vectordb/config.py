from pydantic import BaseModel, AnyUrl, Json


class VectorDBBaseConfigModel(BaseModel):
    url: AnyUrl
    api_key: str
