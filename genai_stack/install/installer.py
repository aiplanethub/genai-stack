from pathlib import Path
import os
import subprocess
import tempfile

from .template_engine import TemplateEngine

BASE_DIR = Path(__file__).parent


class Installer:
    def __init__(
        self,
        component: str,
        sub_component: str,
        options: dict = None,
        quickstart: bool = False,
        output_dir: str = None,
    ) -> None:
        self.component = component
        self.sub_component = sub_component
        self.options = options
        self.quickstart = quickstart
        self.output_dir = output_dir

    def template(self):
        engine = TemplateEngine(
            path=os.path.join(BASE_DIR, "templates"),
            component=self.component,
            sub_component=self.sub_component,
            options=self.options,
            quickstart=self.quickstart,
        )

        return engine.render()

    def write_docker_compose(self, directory):
        temp_dir = Path(directory)
        docker_compose_file = temp_dir / "docker-compose.yaml"
        with open(docker_compose_file, "w+") as compose_file:
            compose_file.write(self.template())

    def install(self):
        if self.output_dir:
            self.run(self.output_dir)
        else:
            dir = tempfile.mkdtemp()
            print(dir)
            self.run(dir)

    def run(self, dir):
        self.write_docker_compose(directory=dir)
        output = subprocess.check_output(
            f"cd {dir} && docker-compose up -d", shell=True, text=True
        )
        print(output)
