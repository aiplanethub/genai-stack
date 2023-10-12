import os
import sys
import subprocess
from pydantic import BaseModel
from pathlib import Path
from jinja2 import FileSystemLoader, Environment

from genai_stack.stack.stack import Stack
from genai_stack.enums import StackComponentType

from .base import BaseETLPlatform


BASE_DIR = Path(__file__).parent


class PrefectPlatformConfig(BaseModel):
    prefect_api_server: str
    runtime_path: str


class PrefectETLPlatform(BaseETLPlatform):
    config_class = PrefectPlatformConfig
    FLOW_TEMPLATE_NAME = "flow.py.j2"

    def setup(self):
        """
        Create deployment flows for all the loaders
        """

        for loader in self.loaders:
            print(loader.config.id)
            self._build_and_deploy_loader(loader)

    def _get_template(self):
        template_dir = os.path.join(BASE_DIR, "templates/")
        env = Environment(loader=FileSystemLoader(template_dir))

        try:
            # Load the template file using the environment instance
            template = env.get_template(self.FLOW_TEMPLATE_NAME)

            return template
        except Exception as e:
            # Handle any exceptions accordingly
            return str(e)

    def _generate_flow_script(self, loader):
        template = self._get_template()
        flow_script_path = os.path.join(self.platform_config.runtime_path, "flow.py")
        with open(flow_script_path, "w+") as f:
            f.write(
                template.render(
                    stack_config={
                        StackComponentType.ETL.value: loader.get_config_data(),
                        StackComponentType.EMBEDDING.value: self.embedding.get_config_data(),
                        StackComponentType.VECTOR_DB.value: self.vectordb.get_config_data(),
                    },
                    flow_name=loader.__class__.__name__ + str(loader.config.id)[:6],
                )
            )
        return flow_script_path

    def _deploy_flow_script(self, flow_script_path):
        output = subprocess.check_output(
            f"cd {self.platform_config.runtime_path} && {sys.executable} {flow_script_path}", shell=True
        )
        return output

    def _build_and_deploy_loader(self, loader):
        script_path = self._generate_flow_script(loader)
        self._deploy_flow_script(script_path)

    def handle_job(self, loader_id, **kwargs):
        try:
            from prefect.deployments import run_deployment
        except ImportError:
            print(
                """
                Prefect is not found. Install prefect with "pip install prefect==2.10.21"
                """
            )
        flow_run = run_deployment(name=loader_id, parameters=kwargs, timeout=0)
        print(flow_run)
