from sqlalchemy import Column, Integer, JSON, ForeignKey, UUID

from genai_stack.genai_store.schemas.base_schemas import TimeStampedSchema

class StackSessionSchema(TimeStampedSchema):
    """
    SQL Schema for Stack Sessions.

    Args:
        stack_id : Integer
        meta_data : JSON 
    """

    __tablename__ = "stack_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)

    stack_id = Column(
        Integer,
        ForeignKey('stacks.id', ondelete='CASCADE'),
        nullable=False
    )

    meta_data = Column(JSON, nullable=False)

