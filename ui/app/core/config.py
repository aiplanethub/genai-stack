from configparser import ConfigParser
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


DEFAULT_APP_CONFIG = os.path.join(BASE_DIR, "app.default.conf")
OVERRIDE_APP_CONFIG = os.path.join(BASE_DIR, "app.conf")

app_config = ConfigParser()


def read_config(parser: ConfigParser, location: str) -> None:
    assert parser.read(location), f"Could not read config {location}"


# Read dphi conf
if os.path.exists(OVERRIDE_APP_CONFIG):
    read_config(app_config, OVERRIDE_APP_CONFIG)
else:
    read_config(app_config, DEFAULT_APP_CONFIG)
