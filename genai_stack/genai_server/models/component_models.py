from pydantic import BaseModel
from typing import  Dict, Optional
from datetime import datetime

from genai_stack.enums import StackComponentType


class StackComponentRequestModel(BaseModel):
    """Stack Component Request Model."""

    type : StackComponentType
    config : Dict
    meta_data: Dict


class StackComponentResponseModel(BaseModel):
    """Stack Component Response Model."""

    id:int
    type : StackComponentType
    config : Dict
    meta_data: Dict
    created_at: datetime
    modified_at: Optional[datetime] 


class StackComponentFilterModel(BaseModel):
    """Stack Component Filter Model"""
    
    id:int


class StackComponentUpdateRequestModel(BaseModel):
    """Stack Component Update Model."""

    type:Optional[StackComponentType] = None
    config:Optional[dict] = None
    meta_data:Optional[dict] = None
