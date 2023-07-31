MODELS_MODULE = "llm_stack.model"
MODEL_CONFIG_KEY = "model"


class Models:
    GPT_35 = "gpt3.5"


AVAILABLE_MODEL_MAPS = {
    # Model Name: "file_name/class_name"
    Models.GPT_35: "gpt3_5/OpenAIGpt35Model",
}
