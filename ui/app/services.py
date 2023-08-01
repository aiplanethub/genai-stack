import requests
from urllib.parse import urljoin

from core.settings import CHAT_HISTORY_URL, BACKEND_URL

HUMAN_ROLE = "user"
AI_ROLE = "assistant"


def parse_chat_history(chat_history: str) -> dict:
    chat_segments = chat_history.split("question")[1:]
    parsed_result = []
    for segment in chat_segments:
        question, answer = segment.split("answer:")
        parsed_result.append({"role": HUMAN_ROLE, "content": question})
        parsed_result.append({"role": AI_ROLE, "content": answer})
    return parsed_result


def get_chat_history():
    url = urljoin(BACKEND_URL, CHAT_HISTORY_URL)
    chat_history = requests.get(url)
    return parse_chat_history(chat_history.json()["result"])
