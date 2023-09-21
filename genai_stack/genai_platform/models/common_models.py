from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TimeStampsModel(BaseModel):
    """Time Stamps Data Model."""

    created_at: datetime
    modified_at: Optional[datetime] 


class BadRequestResponseModel(BaseModel):
    """Data Model for Bad Request Response."""

    detail:str

class NotFoundResponseModel(BaseModel):
    """Data Model for Not Found Response."""

    detail:str
