from genai_stack.utils import import_class
from genai_stack.constants import (
    VECTORDB_MODULE,
    AVAILABLE_VECTORDB_MAPS,
    MEMORY_MODULE,
    AVAILABLE_MEMORY_MAPS,
    LLM_CACHE_MODULE,
    AVAILABLE_LLM_CACHE_MAPS,
    MODELS_MODULE,
    AVAILABLE_MODEL_MAPS,
    EMBEDDING_MODULE,
    AVAILABLE_EMBEDDING_MAPS
)


components_mappers = {
    "vectordb": {
        "module_name": VECTORDB_MODULE,
        "available_maps": AVAILABLE_VECTORDB_MAPS
    },
    "memory": {
        "module_name": MEMORY_MODULE,
        "available_maps": AVAILABLE_MEMORY_MAPS
    },
    "llm_cache": {
        "module_name": LLM_CACHE_MODULE,
        "available_maps": AVAILABLE_LLM_CACHE_MAPS
    },
    "model": {
        "module_name": MODELS_MODULE,
        "available_maps": AVAILABLE_MODEL_MAPS
    },
    "embedding": {
        "module_name": EMBEDDING_MODULE,
        "available_maps": AVAILABLE_EMBEDDING_MAPS
    }
}


# Getting Component Class
def get_component_class(component_name: str, class_name: str):
    component_mapper = components_mappers.get(component_name)

    module_name = component_mapper['module_name']
    # ex: genai_stack.vectordb

    cls_name = component_mapper['available_maps'].get(class_name)
    # ex: weaviate/Weaviate

    cls_path = f"{module_name}.{cls_name.replace('/', '.')}"
    # genai_stack.vectordb.weaviate.Weaviate

    cls = import_class(cls_path)

    return cls


# Creating indexes provided by user
def generate_index_names(stack_id: int, session_id: int, session_indexes: dict = {}) -> dict:
    if not session_indexes.get("indexstore"):
        session_indexes["indexstore"] = "indexstore"

    if not session_indexes.get("memory"):
        session_indexes["memory"] = "memory"

    if not session_indexes.get("cache"):
        session_indexes["cache"] = "cache"

    template = f"{stack_id}-{session_id}"

    return {
        "indexstore": f"{template}-{session_indexes.get('indexstore')}",
        "memory": f"{template}-{session_indexes.get('memory')}",
        "cache": f"{template}-{session_indexes.get('cache')}"
    }


def get_current_stack(config: dict):
    components = {}

    for component_name, component_config in config.get("components").items():
        cls = get_component_class(component_name, component_config.get("name"))
        components[component_name] = cls.from_kwargs(**component_config.get("config"))
    
    # To avoid circular import error
    from genai_stack.stack.stack import Stack
    
    stack = Stack(**components)
    return stack
