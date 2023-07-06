from attrs import define, field, validators

from .base import BaseInstaller


@define
class AirbyteInstaller(BaseInstaller):
    repo_url: str = field(
        validator=validators.instance_of(str),
        default="https://github.com/airbytehq/airbyte.git",
    )
    destination_dir: str = field(
        validator=validators.instance_of(str), default="/tmp/llaim_airbyte"
    )
