from model.gpt3_5 import OpenAIGpt35Model


class Models:
    OPENAI = "openai"


MODEL_NAME_MAP = {Models.OPENAI: OpenAIGpt35Model}
