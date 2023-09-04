from typing import Callable
from pydantic import BaseModel

from genai_stack.stack.stack_component import StackComponent, StackComponentConfig
from genai_stack.vectordb.chromadb.constants import DEFAULT_SEARCH_OPTIONS


class BaseVectorDBConfigModel(BaseModel):
    """Base Data Model for VectorDB"""

    pass


class BaseVectorDBConfig(StackComponentConfig):
    """Base VectorDB Config Stack Component Config"""

    data_model = BaseVectorDBConfigModel


class BaseVectorDB(StackComponent):
    """Base VectorDB Stack Component"""

    config_class = BaseVectorDBConfig
    _search_method: Callable = None
    search_options: dict = DEFAULT_SEARCH_OPTIONS

    @property
    def client(self):
        raise NotImplementedError()

    def query(self):
        raise NotImplementedError()
