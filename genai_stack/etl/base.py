import typing
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

from genai_stack.stack.stack_component import StackComponent, StackComponentConfig


class BaseETLConfigModel(BaseModel):
    """
    Data Model for the configs
    """

    id: UUID = Field(default_factory=uuid4)


class BaseETLConfig(StackComponentConfig):
    data_model = BaseETLConfigModel


class BaseETL(StackComponent):
    config_class = BaseETLConfig

    def _post_init(self, run_etl=True, *args, **kwargs):
        if run_etl:
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
