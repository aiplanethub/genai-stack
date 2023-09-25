import uuid
import os
import json
from pydantic import BaseModel, root_validator
from pathlib import Path
from typing import Optional

from genai_stack.services.base import BaseService
from genai_stack.utils.daemon import Daemon


class LocalServiceConfig(BaseModel):
    """Configuration for the local service

    id: Id of the service
    runtime_path: Path where the log file and the pid file would be stored for the service.
    log_file_name: Name of the log file ending with .log extension
    pid_file_name: Name of the pid file ending with .pid extension
    config_output_path: Path on where to store the config of the service to reload from it.
    """

    id: Optional[str] = str(uuid.uuid4())[:6]
    runtime_path: str
    log_file_name: Optional[str] = f"{id}.log"
    pid_file_name: Optional[str] = f"{id}.pid"
    config_output_path: Optional[str] = None

    @root_validator(pre=False)
    def check_config_output_path(cls, values):
        if not values.get("config_output_path"):
            values["config_output_path"] = values.get("runtime_path")
        return values


class LocalService(BaseService):
    config_class = LocalServiceConfig

    def setup(self):
        self.runtime_dir = os.path.abspath(self.config.runtime_path)
        self.config_file_path = os.path.join(self.config.config_output_path, f"{self.config.id[:6]}.json")
        self.log_file_path = os.path.join(self.runtime_dir, self.config.log_file_name)
        self.pid_file_path = os.path.join(self.runtime_dir, self.config.pid_file_name)
        self.daemon = Daemon(self.run, log_file=self.log_file_path, pid_file=self.pid_file_path)

    def provision(self):
        self.daemon.run_as_daemon()
        self.store_to_registry()

    def deprovision(self):
        self.daemon.stop_daemon(self.pid_file_path)

    def is_running(self):
        """
        Method to check if a service is running or not
        """
        raise NotImplementedError()

    def is_stopped(self):
        """
        Method to check if a service is running or not
        """
        raise NotImplementedError()

    def store_to_registry(self, exclude={"config_output_path"}):
        """
        Currently we store the service related configurations to a json file to the config_output_path location
        """
        config_path_dir = Path(self.config_file_path).parent
        if not os.path.exists(config_path_dir):
            os.makedirs(config_path_dir, exist_ok=True)

        with open(self.config_file_path, "w+") as f:
            json_data = self.config.dict(exclude=exclude)
            json_data.update(self._get_service_metadata())
            json.dump(json_data, f)

    def _get_service_metadata(self):
        """
        Additional metadata you want to save with your service
        """
        return {}

    def get_status(self):
        """
        Get status of the service.
        """
        raise NotImplementedError()

    def run(self):
        """
        Write the logic to be executed as a daemon process in the service
        """
        pass
