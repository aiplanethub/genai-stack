import os
from configparser import ConfigParser

# 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Parse configuration
GENAI_STACK_CONF = os.path.join(BASE_DIR,"genai_stack.conf")


genai_stack_config = ConfigParser()

def read_config(parser:ConfigParser, config_file_location:str) -> None:
    assert parser.read(config_file_location), f"Could not read config {config_file_location}"

# Read secrets conf
read_config(genai_stack_config, GENAI_STACK_CONF)
