from pydantic import BaseModel

from genai_stack.stack.stack_component import StackComponent, StackComponentConfig


class BaseVectorDBConfigModel(BaseModel):
    """Base Data Model for VectorDB"""

    pass


class BaseVectorDBConfig(StackComponentConfig):
    """Base VectorDB Config Stack Component Config"""

    data_model = BaseVectorDBConfigModel


class BaseVectorDB(StackComponent):
    """Base VectorDB Stack Component"""

    config_class = BaseVectorDBConfig

    @property
    def client(self):
        raise NotImplementedError()

    def query(self):
        raise NotImplementedError()
