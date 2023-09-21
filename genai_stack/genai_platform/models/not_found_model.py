from pydantic import BaseModel

class NotFoundResponseModel(BaseModel):
    """Data Model for Not Found Response."""

    detail:str
