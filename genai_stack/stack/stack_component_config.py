from abc import ABCMeta, ABC
from typing import Any
from pydantic import ValidationError


class StackComponentConfig(ABC):
    data_model = None

    def __init__(self, **config_data) -> Any:
        if not self.data_model:
            raise ValueError(
                f"No data model was provided for {self.__class__.__name__}. Every stack component has to specify the data model of its configuration."
            )

        self._data = config_data
        self.config = self.validate()

    def validate(self):
        try:
            data = self.data_model(**self._data)
            return data
        except ValidationError as e:
            raise (e)

    def __getattr__(self, name):
        return getattr(self.config, name)
