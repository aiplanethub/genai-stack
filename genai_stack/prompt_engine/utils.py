import enum
from typing import TypedDict


class ValidationResponseDict(TypedDict):
    decision: bool
    reason: str
    response: str


class PromptTypeEnum(enum.Enum):
    SIMPLE_CHAT_PROMPT = "simple_chat_prompt"
    CONTEXTUAL_CHAT_PROMPT = "contextual_chat_prompt"
    CONTEXTUAL_QA_PROMPT = "contextual_qa_prompt"
