from .config import app_config

BACKEND_URL = app_config.get("llmstack", "backend_url")

CHAT_HISTORY_URL = app_config.get("uri", "chat_history")
PREDICT_URL = app_config.get("uri", "predict")
