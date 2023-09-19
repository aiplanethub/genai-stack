from pydantic import BaseModel

class DeleteResponseModel(BaseModel):
    """Data Model for Delete Response."""

    details:str
