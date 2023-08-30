from typing import TypedDict


class ValidationResponseDict(TypedDict):
    decision: bool
    reason: str
    response: str
