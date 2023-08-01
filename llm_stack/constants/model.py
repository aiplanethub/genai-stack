MODELS_MODULE = "llm_stack.model"
MODEL_CONFIG_KEY = "model"


class Models:
    GPT_35 = "gpt3.5"
    GPT4ALL = "gpt4all"


AVAILABLE_MODEL_MAPS = {
    # Model Name: "file_name/class_name"
    Models.GPT_35: "gpt3_5/OpenAIGpt35Model",
    Models.GPT4ALL: "gpt4all/Gpt4AllModel",
}

DEFAULT_MODEL_JSON = {
    "model": {
        "name": "gpt4all",
        "fields": {
            "model": "ggml-gpt4all-j-v1.3-groovy",
        },
    },
}
