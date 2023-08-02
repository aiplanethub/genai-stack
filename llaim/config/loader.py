import json
import logging
from pathlib import Path
import typing


class ConfigLoader:
    name: str
    config: str

    def __init__(self, name: str = "ConfigLoader", config: str = None) -> None:
        """Initializes the instances based on the name and config

        Args:
            name: A string to name the config loader class
            config: A string that holds the json file path which contains the configs
                    required to load a json config file.
        """
        self.name = name
        self.config = config
        self.load_config()

    @staticmethod
    def _read_json_file(file_path: str):
        with open(file_path) as file:
            data = json.load(file)
        return data

    def load_config(self):
        """Loads the configs and can set as class attrs"""
        logging.info("Loading Configs")

        f = Path(self.config)

        if not f.exists():
            raise ValueError(
                f"Unable to find the file. Input given - {self.config}",
            )

        try:
            f = self._read_json_file(f.absolute())
            self.config_dict = f
        except json.JSONDecodeError as e:
            raise ValueError("Unable to read the config file.") from e

    def parse_config(self, config_key: str, compulsory_fields=typing.List[str]):
        config = self.config.get(config_key, None)
        if not config:
            raise ValueError(f"{config_key} config not found.")

        config_fields = config.get("fields", None)

        if not config_fields and compulsory_fields:
            raise ValueError(
                f"Config fields are missing for {config_key} config."
                f"There are some compulsory fields that needs to be present for this config they are {compulsory_fields}"
            )
        absent_compulsory_fields = []

        # Check if all compulsory fields are present either in the fields section or in the 
        if compulsory_fields:
            absent_compulsory_fields = [
                compulsory_field
                for compulsory_field in compulsory_fields
                if compulsory_field not in (config_fields.keys() + config.keys())
            ]
            raise ValueError(f"Compulsory fields {absent_compulsory_fields} are missing from your config.")

        setattr(self, f"{config_key}_config", config)
        setattr(self, f"{config_key}_config_fields", config_fields)

    def run(self):
        """This method should contain the actual logic for creating the EtL pipeline"""
        raise NotImplementedError
