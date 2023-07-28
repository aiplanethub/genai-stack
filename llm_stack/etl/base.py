import json
import logging
from pathlib import Path

from .exception import llm_stackEtlException


class EtlBase:
    name: str
    config: str

    def __init__(self, name: str = "EtlBase", config: str = None) -> None:
        """Initializes the instances based on the name and config

        Args:
            name: A string to name the ETL class
            config: A string that holds the json file path which contains the configs
                    required to setup airbyte connection.
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
            raise llm_stackEtlException(
                f"Unable to find the file. Input given - {self.config}",
            )

        try:
            f = self._read_json_file(f.absolute())
            self.config_dict = f
        except json.JSONDecodeError as e:
            raise llm_stackEtlException("Unable to read the config file.") from e

    def run(self):
        """This method should contain the actual logic for creating the EtL pipeline"""
        raise NotImplementedError
