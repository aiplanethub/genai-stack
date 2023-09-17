from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship
from typing import List

from genai_stack.genai_store.schemas.base_schemas import TimeStampedSchema
from genai_stack.genai_store.schemas.component_schemas import StackComponentSchema
from genai_stack.genai_server.models.constants import STR_FIELD_MAX_LENGTH


class StackSchema(TimeStampedSchema):
    """
    SQL Schema for Stacks.

    Args:
        name : String
        description : String
    """
    
    __tablename__ = "stacks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(STR_FIELD_MAX_LENGTH), nullable=False)
    description = Column(String(STR_FIELD_MAX_LENGTH), nullable=False)

    components:List["StackComponentSchema"] = Relationship(
        "StackComponentSchema", 
        secondary="stack_compositions",
    )