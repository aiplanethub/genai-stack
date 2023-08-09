import os
from configparser import ConfigParser
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

SERVER_CONF = os.path.join(BASE_DIR, "server.conf")

server_config = ConfigParser()


def read_config(parser: ConfigParser, location: str) -> None:
    assert parser.read(location), f"Could not read config {location}"


# Read server conf
if os.path.exists(SERVER_CONF):
    read_config(server_config, SERVER_CONF)
else:
    raise ValueError(f"Server config file was not found at {SERVER_CONF}")
