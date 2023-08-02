import pathlib
from attrs import define, field, validators

from git import Repo, RemoteProgress

from llaim import LLAIM_DEBUG


class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=""):
        print(self._cur_line)
        super().update()


@define
class BaseInstaller:
    repo_url: str = field(validator=validators.instance_of(str))
    destination_dir: str = field(validator=validators.instance_of(str))

    @classmethod
    def create_directory(cls, directory: str):
        pathlib.Path(directory).mkdir(parents=True, exist_ok=True)

    def _git_clone_airbyte(self):
        Repo.clone_from(self.repo_url, self.destination_dir, progress=Progress())

    def install(self, stream_output: LLAIM_DEBUG):
        # Clonse the repo
        self._git_clone_airbyte()
