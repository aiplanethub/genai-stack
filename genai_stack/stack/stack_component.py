import json
from abc import ABC
from pathlib import Path

from genai_stack.stack.stack_component_config import StackComponentConfig
from genai_stack.stack.mediator import Mediator


class StackComponent(ABC):
    """Base Component class for all other stack components"""

    config_class = StackComponentConfig

    def __init__(self, config: StackComponentConfig, mediator=None) -> None:
        """Initialize the stack component

        Args:
            config: The StackComponentConfig for this StackComponent
            mediator: Mediator which handles all the inter component communication in the stack
        """
        self._config = config
        self._mediator: Mediator = mediator
        self._post_init()

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator

    @property
    def config(self):
        return self._config

    @classmethod
    def from_config_file(cls, config_file_path: str):
        """Loads the configs and initialises the StackComponent from a json file"""
        cls._check_config_class()

        f = Path(config_file_path)

        if not f.exists():
            raise ValueError(
                f"Unable to find the file. Input given - {config_file_path}",
            )

        try:
            with open(f.absolute()) as file:
                data = cls.config_class(**json.load(file))
                return cls(data)

        except json.JSONDecodeError as e:
            raise ValueError("Unable to read the config file.") from e

    @classmethod
    def from_kwargs(cls, **kwargs):
        """
        Loads the configs and initialises the StackComponent from kwargs
        """
        cls._check_config_class()
        return cls(cls.config_class(**kwargs))

    @classmethod
    def _check_config_class(cls):
        if not cls.config_class:
            raise ValueError(f"Config class not defined for component {cls.__name__}")

    def _post_init(self, *args, **kwargs):
        """
        Override this method if you want to extend the functionality of the init function
        """
        pass
