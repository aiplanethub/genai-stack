import json
import logging
from pathlib import Path
import typing
from genai_stack.constants.config import GLOBAL_REQUIRED_FIELDS


class ConfigLoader:
    name: str
    config: str

    def __init__(self, name: str = "ConfigLoader", config: typing.Union[str, dict] = None) -> None:
        """Initializes the instances based on the name and config

        Args:
            name: A string to name the config loader class
            config: A string that holds the json file path which contains the configs
                    required to load a json config file.
        """
        self.name = name
        self._config = config
        self.load_config()

    @staticmethod
    def _read_json_file(file_path: str):
        with open(file_path) as file:
            data = json.load(file)
        return data

    def load_config(self):
        """Loads the configs and can set as class attrs"""
        logging.info("Loading Configs")

        if isinstance(self._config, dict):
            self.config = self._config
            return

        f = Path(self._config)

        if not f.exists():
            raise ValueError(
                f"Unable to find the file. Input given - {self._config}",
            )

        try:
            f = self._read_json_file(f.absolute())
            self.config = f
        except json.JSONDecodeError as e:
            raise ValueError("Unable to read the config file.") from e

    def parse_config(self, config_key: str, required_fields: typing.List[str] = None):
        config = self.config.get(config_key, None)
        if config is None:
            raise ValueError(f"{config_key} config not found.")

        config_fields = config.get("fields", {})
        absent_required_fields = []

        # Check if all compulsory fields are present either in the fields section or in the
        if required_fields:
            if absent_required_fields := [
                required_field
                for required_field in required_fields
                if required_field not in (list(config_fields.keys()) + list(config.keys()))
            ]:
                raise ValueError(
                    f"Compulsory fields {absent_required_fields} are missing from your '{config_key}' config."
                )

        setattr(self, f"{config_key}_config", config)
        setattr(self, f"{config_key}_config_fields", config_fields)

    def get_config_section_name(self, config_section: str):
        config_section = self.get_config_section(config_section)
        if not config_section:
            raise ValueError(f"Config Section {config_section} does not exist. Please check your config file")

        if name := config_section.get("name", None):
            return name
        else:
            raise ValueError(f"Name not found for config section {config_section}")

    def get_config_section(self, config_section: str):
        return self.config.get(config_section, None)

    def run(self):
        """This method should contain the actual logic for creating the EtL pipeline"""
        raise NotImplementedError
