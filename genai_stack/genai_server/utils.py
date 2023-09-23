from sqlalchemy.orm import Session

from genai_stack.genai_store.schemas.session_schemas import StackSessionSchema
from genai_stack.genai_store.sql_store import SQLStore

from genai_stack.enums import StackComponentType
from genai_stack.stack.stack import Stack
from genai_stack.utils import import_class

STORE = SQLStore()


def EmbeddingFactory(component_config):
    _MAP = {
        "langchain": "genai_stack.embedding.langchain"
    }

    cls = import_class(_MAP.get(component_config.get("name")))
    return cls.from_kwargs(component_config)


def VectordbFactory(component_config):
    _MAP = {
        "weaviate": "genai_stack.vectordb.weaviate",
        "chromadb": "genai_stack.vectordb.chromadb"
    }
    cls = import_class(_MAP.get(component_config.get("name")))
    return cls.from_kwargs(component_config)


def RetrieverFactory(component_config):
    _MAP = {
        "langchain": "genai_stack.retriever.langchain"
    }
    cls = import_class(_MAP.get(component_config.get("name")))
    return cls.from_kwargs(component_config)


factory_map = {
    StackComponentType.EMBEDDING: EmbeddingFactory,
    StackComponentType.VECTOR_DB: VectordbFactory,
    StackComponentType.RETRIEVER: RetrieverFactory,
}


def default_override_handler(config, override):
    config.update(override)


def vectordb_config_handler(config, override, session_id):
    with Session(STORE.engine) as session:
        stack_session = session.get(StackSessionSchema(
            stack_id=1,
            session_id=session_id
        ))
        override = stack_session.metadata.get(StackComponentType.VECTOR_DB)
        config.update(override)


def retriever_config_handler(config, override, session_id):
    with Session(STORE.engine) as session:
        stack_session = session.get(StackSessionSchema)
        override = stack_session.metadata.get(StackComponentType.RETRIEVER)
        config.update(override)


override_handler_map = {
    "default": default_override_handler,
    StackComponentType.VECTOR_DB: vectordb_config_handler,
    StackComponentType.RETRIEVER: retriever_config_handler,
}


def get_component(component_name, component_config):
    factory = factory_map.get(component_name)
    return factory(component_config)


def get_current_stack(config, overrides, session_id):
    component_dict = {}
    for component_name, component_config in config.items():
        # Override component configs if necessary
        override_handler = override_handler_map.get(component_name, None) or default_override_handler
        override_handler(component_config, overrides, session_id)

        component_dict[component_name] = get_component(component_config)

    Stack(model=None, **component_dict)
