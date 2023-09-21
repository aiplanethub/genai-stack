from sqlalchemy import Column, Integer, JSON, ForeignKey, UUID

from genai_stack.genai_store.schemas.base_schemas import TimeStampedSchema

class StackSessionSchema(TimeStampedSchema):
    """
    SQL Schema for Stack Sessions.

    Args:
        stack_id : Integer
        session_metadata : JSON 
    """

    __tablename__ = "stack_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)

    stack_id = Column(
        Integer,
        ForeignKey('stacks.id', ondelete='CASCADE'),
        nullable=False
    )

    session_metadata = Column(JSON, nullable=False)

