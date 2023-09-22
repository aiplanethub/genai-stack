from pydantic import BaseModel
from typing import  Dict, Optional

from genai_stack.enums import StackComponentType
from genai_stack.genai_platform.models import TimeStampsModel


class StackComponentBaseModel(BaseModel):
    """Stack Component Base Data Model."""

    type : StackComponentType
    config : Dict
    meta_data: Dict


class StackComponentRequestModel(StackComponentBaseModel):
    """
    Stack Component Request Data Model.

    Args:
        type : StackComponentType
        config : dict
        meta_data : dict
    """


class StackComponentResponseModel(StackComponentBaseModel, TimeStampsModel):
    """
    Stack Component Response Data Model.
    
    Args:
        id : int,
        type : StackComponentType,
        config : dict,
        meta_data : dict,
        created_at : datetime
        modified_at : datetime
    """

    id:int


class StackComponentFilterModel(BaseModel):
    """
    Stack Component Filter Data Model.

    Args:
        id : int
    """
    
    id:int


class StackComponentUpdateRequestModel(BaseModel):
    """
    Stack Component Update Data Model.
    
    Args:
        type : Optional[StackComponentType]
        config : Optional[dict]
        meta_data : Optional[dict]
    """

    type:Optional[StackComponentType] = None
    config:Optional[dict] = None
    meta_data:Optional[dict] = None
