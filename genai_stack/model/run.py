from genai_stack.core import ConfigLoader
from genai_stack.utils.importing import import_class
from genai_stack.constants.model import (
    MODEL_CONFIG_KEY,
    MODELS_MODULE,
    AVAILABLE_MODEL_MAPS,
)
from genai_stack.constants.retriever import RETRIEVER_MODULE, AVAILABLE_RETRIEVER_MAPS
from genai_stack.constants.vectordb import VECTORDB_MODULE, AVAILABLE_VECTORDB_MAPS
from genai_stack.utils.importing import import_class_from_file
from genai_stack.constants.config import CUSTOM_MODEL_CONFIG_FIELDS
from fastapi.responses import JSONResponse


def list_supported_models():
    return AVAILABLE_MODEL_MAPS.keys()


def _get_class(module: str, map: str, class_name: str):
    return import_class(f"{module}.{map.get(class_name).replace('/','.')}")  # noqa: E501


def get_model_class(model_name: str):
    return _get_class(MODELS_MODULE, AVAILABLE_MODEL_MAPS, model_name)


def get_retriever_class(retriever_name: str):
    return _get_class(RETRIEVER_MODULE, AVAILABLE_RETRIEVER_MAPS, retriever_name)


def get_vectordb_class(vectordb_name: str):
    return _get_class(VECTORDB_MODULE, AVAILABLE_VECTORDB_MAPS, vectordb_name)


def run_custom_model(config_file: str, config_loader: ConfigLoader, retriver):
    def _get_server_params(model_config_fields: dict):
        return {
            "response_class": import_class(
                f"fastapi.responses.{model_config_fields.get(CUSTOM_MODEL_CONFIG_FIELDS.RESPONSE_CLASS, JSONResponse)}",  # noqa: E501
            ),
            "host": model_config_fields.get(
                CUSTOM_MODEL_CONFIG_FIELDS.HOST,
                "127.0.0.1",
            ),
            "port": model_config_fields.get(CUSTOM_MODEL_CONFIG_FIELDS.PORT, 8082),
        }

    config_loader.parse_config(
        config_key=MODEL_CONFIG_KEY,
        required_fields=[
            CUSTOM_MODEL_CONFIG_FIELDS.CLASS_NAME,
            CUSTOM_MODEL_CONFIG_FIELDS.FILE_PATH,
        ],
    )
    model_config_fields: dict = getattr(config_loader, "model_config_fields", None)
    cls_name = model_config_fields.get(CUSTOM_MODEL_CONFIG_FIELDS.CLASS_NAME)
    file_path = model_config_fields.get(CUSTOM_MODEL_CONFIG_FIELDS.FILE_PATH)

    cls = import_class_from_file(file_path=file_path, class_name=cls_name)(
        config=config_file,
        retriever=retriver,
    )
    cls.load(model_path=model_config_fields.get("model_path"))
    cls.run_http_server(**_get_server_params(model_config_fields=model_config_fields))
