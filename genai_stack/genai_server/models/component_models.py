from pydantic import BaseModel
from typing import  Dict
from datetime import datetime

from genai_stack.enums import StackComponentType

class StackComponentBaseModel(BaseModel):
    """Base Model for the Stack Component."""
    type : StackComponentType
    config : Dict

class StackComponentRequestModel(StackComponentBaseModel):
    """Stack Component Request Model."""
    pass


class StackComponentResponseModel(StackComponentBaseModel):
    """Stack Component Response Model."""
    id:int
    created_at: datetime
    modified_at: datetime
    metadata:Dict


class StackComponentFilterModel(BaseModel):
    """Stack Component Filter Model"""
    id:int
    type:StackComponentType
