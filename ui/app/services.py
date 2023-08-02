import requests
from urllib.parse import urljoin

from core.settings import CHAT_HISTORY_URL, BACKEND_URL, PREDICT_URL

HUMAN_ROLE = "user"
AI_ROLE = "assistant"


def parse_chat_history(chat_history: str) -> dict:
    chat_segments = chat_history.split("question")[1:]
    parsed_result = []
    for segment in chat_segments:
        try:
            question, answer = segment.split("answer:")
            parsed_result.append({"role": HUMAN_ROLE, "content": question})
            parsed_result.append({"role": AI_ROLE, "content": answer})
        except ValueError:
            print("Unparsable segment >>>>>>>>>>>", segment)
    return parsed_result


def parse_chat_response(chat_response: dict) -> str:
    result = chat_response["result"]


def get_chat_history():
    url = urljoin(BACKEND_URL, CHAT_HISTORY_URL)
    chat_history = requests.get(url)

    return parse_chat_history(chat_history.json()["result"])


def get_response(prompt: str):
    url = urljoin(BACKEND_URL, PREDICT_URL)
    response = requests.post(url, data={"query": prompt}).json()
    return response
