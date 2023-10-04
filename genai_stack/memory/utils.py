from typing import List, Dict
from langchain.schema.messages import BaseMessage


def get_chat_conversation_history_dict(messages: List[BaseMessage]) -> List[Dict]:
    """
    Converts a list of messages into a list of dictionaries representing a chat conversation history.

    Args:
        messages (List[BaseMessage]): The list of messages.

    Returns:
        List[Dict]: The formatted chat conversation history.

    Example:
        ```python
        messages = [BaseMessage(), BaseMessage()]

        # Converting the list of messages into a chat conversation history
        history = get_chat_conversation_history_dict(messages)
        print(history)
        ```
    """

    formatted_messages = []
    for i in range(0, len(messages), 2):
        user_message = messages[i].content
        model_message = messages[i + 1].content

        formatted_messages.append({"user_text": user_message, "model_text": model_message})
    return formatted_messages


def parse_chat_conversation_history(response: list) -> str:
    history = ""
    for i in range(len(response)):
        if i % 2 == 0:
            history += f"HUMAN : {response[i].content}\n"
        else:
            history += f"YOU : {response[i].content}\n"

    return history
