from llaim.utils.importing import import_class
from llaim.constants.model import MODELS_MODULE, AVAILABLE_MODEL_MAPS
from llaim.constants.retriever import RETRIEVER_MODULE, AVAILABLE_RETRIEVER_MAPS
from llaim.constants.vectordb import VECTORDB_MODULE, AVAILABLE_VECTORDB_MAPS


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
