from pydantic import BaseModel

class BadRequestResponseModel(BaseModel):
    """Data Model for Bad Request Response."""

    detail:str