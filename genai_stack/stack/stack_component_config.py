from abc import ABCMeta, ABC
from pydantic import BaseModel
from typing import Any
from pydantic import ValidationError


class StackComponentConfig(ABC):
    data_model: BaseModel = None

    def __init__(self, **config_data) -> Any:
        if not self.data_model:
            raise ValueError(
                f"No data model was provided for {self.__class__.__name__}. Every stack component has to specify the data model of its configuration."
            )

        self._data = config_data  # Raw data
        self._config = self.validate()  # Validated data

    def validate(self):
        try:
            data = self.data_model(**self._data)
            return data
        except ValidationError as e:
            raise (e)

    @property
    def config_data(self):
        return self._config

    def __getattr__(self, name):
        return getattr(self._config, name)
