from pydantic import BaseModel, Field
from typing import List, Dict
from datetime import datetime

from genai_stack.genai_server.models.constants import STR_FIELD_MAX_LENGTH

class StackBaseModel(BaseModel):
    """Base Model for the Stack"""

    name:str = Field(
        title="The name of the stack.", max_length=STR_FIELD_MAX_LENGTH
    )
    description:str = Field(
        default="",
        title="The description of the stack",
        max_length=STR_FIELD_MAX_LENGTH,
    )


class StackRequestModel(StackBaseModel):
    """Stack Request Model"""
    pass


class StackResponseModel(StackBaseModel):
    """Stack Response Model"""
    id:int
    stack_components: List
    created_at: datetime
    modified_at: datetime
    metadata:Dict


class StackFilterModel(BaseModel):
    """Stack Filter Model"""
    id:int
    name:str
