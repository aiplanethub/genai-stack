from pydantic import BaseModel

from genai_stack.stack.stack_component import StackComponent, StackComponentConfig


class BaseVectorDBConfigModel(BaseModel):
    """Base Data Model for VectorDB"""

    pass


class BaseVectorDBConfig(StackComponentConfig):
    """Base VectorDB Config Stack Component Config"""

    db_parameters = BaseVectorDBConfigModel


class BaseVectorDB(StackComponent):
    """Base VectorDB Stack Component"""

    config_class = BaseVectorDBConfig

    def get_client(self):
        raise NotImplementedError

    def search(self):
        raise NotImplementedError
