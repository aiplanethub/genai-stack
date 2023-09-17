from sqlalchemy import Column, Integer, ForeignKey
from genai_stack.genai_store.schemas.base_schemas import TimeStampedSchema

class StackCompositionSchema(TimeStampedSchema):
    """
    SQL Schema for Stack Compositions.

    Args:
        stack_id : Integer
        component_id : Integer
    
    Join table between Stacks and StackComponents.
    """

    __tablename__ = "stack_compositions"

    stack_id = Column(
        Integer,
        ForeignKey('stacks.id', ondelete='CASCADE'),
        nullable=False,
        primary_key=True
    )
    
    component_id = Column(
        Integer,
        ForeignKey('components.id', ondelete='CASCADE'),
        nullable=False,
        primary_key=True
    )