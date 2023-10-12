from genai_stack.utils import import_class
from genai_stack.enums import StackComponentType
from genai_stack.constants import (
    ETL_MODULE,
    AVAILABLE_ETL_LOADERS,
    VECTORDB_MODULE,
    AVAILABLE_VECTORDB_MAPS,
    MEMORY_MODULE,
    AVAILABLE_MEMORY_MAPS,
    LLM_CACHE_MODULE,
    AVAILABLE_LLM_CACHE_MAPS,
    MODELS_MODULE,
    AVAILABLE_MODEL_MAPS,
    EMBEDDING_MODULE,
    AVAILABLE_EMBEDDING_MAPS,
    RETRIEVER_MODULE,
    AVAILABLE_RETRIEVER_MAPS,
    PROMPT_ENGINE_MODULE,
    AVAILABLE_PROMPT_ENGINE_MAPS,
)


components_mappers = {
    StackComponentType.ETL: {"module_name": ETL_MODULE, "available_maps": AVAILABLE_ETL_LOADERS},
    StackComponentType.VECTOR_DB: {"module_name": VECTORDB_MODULE, "available_maps": AVAILABLE_VECTORDB_MAPS},
    StackComponentType.MEMORY: {"module_name": MEMORY_MODULE, "available_maps": AVAILABLE_MEMORY_MAPS},
    StackComponentType.CACHE: {"module_name": LLM_CACHE_MODULE, "available_maps": AVAILABLE_LLM_CACHE_MAPS},
    StackComponentType.MODEL: {"module_name": MODELS_MODULE, "available_maps": AVAILABLE_MODEL_MAPS},
    StackComponentType.EMBEDDING: {"module_name": EMBEDDING_MODULE, "available_maps": AVAILABLE_EMBEDDING_MAPS},
    StackComponentType.PROMPT_ENGINE: {
        "module_name": PROMPT_ENGINE_MODULE,
        "available_maps": AVAILABLE_PROMPT_ENGINE_MAPS,
    },
    StackComponentType.RETRIEVER: {"module_name": RETRIEVER_MODULE, "available_maps": AVAILABLE_RETRIEVER_MAPS},
}


# Getting Component Class
def get_component_class(component_name: str, class_name: str):
    component_mapper = components_mappers.get(component_name)
    module_name = component_mapper["module_name"]
    # ex: genai_stack.vectordb
    cls_name = component_mapper["available_maps"].get(class_name)
    # ex: weaviate/Weaviate
    cls_path = f"{module_name}.{cls_name.replace('/', '.')}"
    # genai_stack.vectordb.weaviate.Weaviate

    cls = import_class(cls_path)

    return cls


def get_stack_from_config(config: dict):
    from genai_stack.stack.stack import Stack

    components = {}

    for component_name, component_config in config.get("components").items():
        cls = get_component_class(component_name, component_config.get("name"))
        configurations: dict = component_config.get("config")
        components[component_name] = cls.from_kwargs(**configurations)

    stack = Stack(**components, run_etl=False)
    return stack
