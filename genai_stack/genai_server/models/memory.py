from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    """
    Represents a message with user text and model text.

    Attributes:
        user_text (str): The text provided by the user.
        model_text (str): The text generated by the model.
    """

    user_text: str
    model_text: str


class MemoryBaseModel(BaseModel):
    """
    Represents a base model for memory with a session ID.

    Attributes:
        session_id (int): The ID of the session.
    """

    session_id: int


class MemoryAddTextRequestModel(MemoryBaseModel):
    """
    Represents a request model for adding text to memory, extending the MemoryBaseModel.

    Attributes:
        message (Message): The message containing user text and model text.
    """

    message: Message


class MemoryLatestMessageResponseModel(MemoryBaseModel):
    """
    Represents a response model for the latest message in memory, extending the MemoryBaseModel.

    Attributes:
        message (Optional[Message]): The latest message in memory, if available.
    """

    message: Optional[Message]


class MemoryHistoryResponseModel(MemoryBaseModel):
    """
    Represents a response model for the history of messages in memory, extending the MemoryBaseModel.

    Attributes:
        messages (Optional[List[Message]]): The list of messages in memory, if available.
    """

    messages: Optional[List[Message]]
