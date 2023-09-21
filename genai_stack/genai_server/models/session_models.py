from pydantic import BaseModel
from typing import Dict

from genai_stack.genai_platform.models.common_models import TimeStampsModel

class StackSessionBaseModel(BaseModel):
    """Stack Session Base Data Model."""

    stack_id:int
    meta_data:Dict

class StackSessionRequestModel(StackSessionBaseModel):
    """
    Stack Session Request Data Model.

    Args:
        stack_id : int
        meta_data : dict
    """

class StackSessionResponseModel(StackSessionBaseModel, TimeStampsModel):
    """
    Stack Session Response Data Model.

    Args:
        id : int
        stack_id : int
        meta_data : dict
        created_at : datetime
        modified_at : datetime
    """

    id:int


class StackSessionFilterModel(BaseModel):
    """
    Stack Session Filter Data Model.

    Args:
        id : int
    """
    
    id:int


    