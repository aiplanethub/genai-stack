from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TimeStampsModel(BaseModel):
    """Time Stamps Data Model."""

    created_at: datetime
    modified_at: Optional[datetime] 


class DetailResponseModel(BaseModel):
    """Details Response Data Model."""

    detail:str


class BadRequestResponseModel(DetailResponseModel):
    """
    Bad Request Response Data Model.

    Args:
        detail : str
    """


class NotFoundResponseModel(DetailResponseModel):
    """
    Not Found Response Data Model.

    Args:
        detail : str
    """


class DeleteResponseModel(DetailResponseModel):
    """
    Delete Response Data Model.

    Args:
        detail : str
    """