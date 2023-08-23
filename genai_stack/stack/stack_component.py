import json
from abc import ABC
from pathlib import Path

from genai_stack.stack.stack_component_config import StackComponentConfig


class StackComponent(ABC):
    """Base Component class for all other stack components"""

    def __init__(self, config: StackComponentConfig, mediator=None) -> None:
        """Initialize the stack component

        Args:
            config: The StackComponentConfig for this StackComponent
            mediator: Mediator which handles all the inter component communication in the stack
        """
        self._config = config
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator
    
    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

    @staticmethod
    def config_class() -> StackComponentConfig:
        return StackComponentConfig
    
    

    @classmethod
    def from_config_file(cls, config_file_path: str):
        """Loads the configs and initialises the StackComponent from a json file"""

        f = Path(config_file_path)

        if not f.exists():
            raise ValueError(
                f"Unable to find the file. Input given - {config_file_path}",
            )

        try:
            with open(f.absolute()) as file:
                data = cls.config_class()(**json.load(file))
                return cls(data)

        except json.JSONDecodeError as e:
            raise ValueError("Unable to read the config file.") from e

    @classmethod
    def from_kwargs(cls, **kwargs):
        """
        Loads the configs and initialises the StackComponent from kwargs
        """
        return cls(cls.config_class()(**kwargs))
