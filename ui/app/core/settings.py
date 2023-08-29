from .config import app_config

BACKEND_URL = app_config.get("genai-stack", "backend_url")

CHAT_HISTORY_URL = app_config.get("uri", "chat_history")
PREDICT_URL = app_config.get("uri", "predict")
