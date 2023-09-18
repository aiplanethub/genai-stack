from sqlalchemy import Column, Integer, Enum, JSON
from sqlalchemy.orm import Relationship

from genai_stack.genai_store.schemas.base_schemas import TimeStampedSchema
from genai_stack.enums import StackComponentType


class StackComponentSchema(TimeStampedSchema):
    """
    SQL Schema for Stack Components.

    Args: 
        type : StackComponentType
        config : JSON
        meta_data : JSON
    """

    __tablename__ = "stack_components"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum(StackComponentType), nullable=False)
    config = Column(JSON, nullable=False)
    meta_data = Column(JSON, nullable=False)

    stack = Relationship(
        "StackSchema", 
        secondary="stack_compositions", 
        back_populates="components", 
        uselist=False,
        passive_deletes=True
    )