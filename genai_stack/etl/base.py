import typing
from pydantic import BaseModel

from genai_stack.stack.stack_component import StackComponent, StackComponentConfig


class BaseETLConfigModel(BaseModel):
    """
    Data Model for the configs
    """

    pass


class BaseETLConfig(StackComponentConfig):
    data_model = BaseETLConfigModel


class BaseETL(StackComponent):
    config_class = BaseETLConfig

    def _post_init(self, *args, **kwargs):
        self.run()

    def extract(self) -> typing.Union[str, typing.List[str]]:
        """
        This method extracts the data from the data_source specified from the configs
        """

        raise NotImplementedError()

    def transform(self, data: typing.Union[str, typing.List[str]]) -> typing.Any:
        """
        This method transforms the data into vector embeddings.
        """
        raise NotImplementedError()

    def load(self, data) -> None:
        """
        Load the transformed data into the vectordb
        """
        raise NotImplementedError()

    def run(self):
        self.extract()
        self.transform()
        self.load()
