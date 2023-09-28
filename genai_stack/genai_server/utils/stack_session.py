from fastapi import HTTPException
from sqlalchemy.orm import Session

from genai_stack.genai_server.schemas import StackSessionSchema


def get_stack_session(db_session: Session, stack_session_id: int):
    stack_session = db_session.get(StackSessionSchema, stack_session_id)
    if stack_session is None:
        raise HTTPException(status_code=404, detail=f"Session {stack_session_id} not found")
    return stack_session
