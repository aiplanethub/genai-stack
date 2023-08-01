import requests
from urllib.parse import urljoin

from ui.app.core.settings import CHAT_HISTORY_URL, BACKEND_URL


def get_chat_history():
    url = urljoin(BACKEND_URL, CHAT_HISTORY_URL)
    chat_history = requests.get(url)
    return chat_history
