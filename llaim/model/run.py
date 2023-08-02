from llaim.utils.importing import import_class

MODELS_MODULE = "llaim.model"
AVAILABLE_MODEL_MAPS = {
    # Model Name: "file_name/class_name"
    "gpt3.5": "gpt3_5/OpenAIGpt35Model",
}


def list_supported_models():
    return AVAILABLE_MODEL_MAPS.keys()


def get_model_class(model_name: str):
    return import_class(f"{MODELS_MODULE}.{AVAILABLE_MODEL_MAPS.get(model_name).replace('/','.')}")  # noqa: E501
