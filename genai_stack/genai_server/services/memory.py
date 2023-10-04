from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from genai_stack.genai_server.models.memory import (
    MemoryAddTextRequestModel,
    MemoryHistoryResponseModel,
    MemoryLatestMessageResponseModel,
)
from genai_stack.genai_server.schemas import StackSessionSchema
from genai_stack.genai_server.settings.config import stack_config
from genai_stack.genai_server.utils.utils import get_current_stack


class MemoryService:
    """
    Represents a service for managing memory for chat like conversation.
    """

    def _get_stack_session(self, session, data):
        """
        Retrieves the stack session based on the provided session and data.

        Args:
            session: The session object.
            data: The data containing the session ID.

        Returns:
            The result of retrieving the current stack.

        Raises:
            HTTPException: Raised when the stack session is not found.

        """

        stack_session = session.get(StackSessionSchema, data.session_id)
        if stack_session is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Session {data.session_id} not found",
            )
        return get_current_stack(config=stack_config, session=stack_session)

    def add_to_memory(self, data: MemoryAddTextRequestModel):
        """
        Adds text to memory based on the provided data.

        Args:
            data (MemoryAddTextRequestModel): The data containing the text to be added.

        Returns:
            MemoryLatestMessageResponseModel: The response model containing the latest message in memory.

        Raises:
            HTTPException: Raised when both human and model texts are not provided.
        """

        with Session(self.engine) as session:
            stack = self._get_stack_session(session, data)
            human_text, model_text = data.message.user_text, data.message.model_text

            if not human_text or not model_text:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Both Human and Model texts are required.",
                )

            stack.memory.add_text(user_text=human_text, model_text=model_text)
            response = stack.memory.get_text()
            return MemoryLatestMessageResponseModel(
                message=response,
                session_id=data.session_id,
            )

    def get_memory_history(self, data):
        """
        Retrieves the history of messages in memory based on the provided data.

        Args:
            data: The data containing the session ID.

        Returns:
            MemoryHistoryResponseModel: The response model containing the history of messages in memory.
        """

        with Session(self.engine) as session:
            stack = self._get_stack_session(session, data)
            response = stack.memory.get_chat_history_list()
            return MemoryHistoryResponseModel(
                messages=response,
                session_id=data.session_id,
            )

    def get_latest_message_from_memory(self, data):
        """
        Retrieves the latest message from memory based on the provided data.

        Args:
            data: The data containing the session ID.

        Returns:
            MemoryLatestMessageResponseModel: The response model containing the latest message in memory.

        Example:
            ```python
            data = DataImplementation()

            # Creating an instance of MemoryService
            service = MemoryService()

            # Retrieving the latest message from memory
            response = service.get_latest_message_from_memory(data)
            print(response)
            ```
        """

        with Session(self.engine) as session:
            stack = self._get_stack_session(session, data)
            response = stack.memory.get_text()
            return MemoryLatestMessageResponseModel(
                message=response,
                session_id=data.session_id,
            )
