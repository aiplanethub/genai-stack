from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
from genai_stack.genai_store.app import session

BaseSchema = declarative_base()

BaseSchema.query = session.query_property()

class TimeStampedSchema(BaseSchema):
    """
    SQL Schema for Time Stamps.

    Args:
        created_at  : DateTime
        modified_at : DateTime
    """
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow())
    modified_at = Column(DateTime, onupdate=datetime.utcnow())

