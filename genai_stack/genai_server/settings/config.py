import json
from configparser import ConfigParser


# Storing the runtime path
path:str = ""


# For reading stack config
stack_config = {}

def read_stack_config(run_time_path:str) -> dict:
    """This method for reading stack configs."""
    
    STACK_CONFIG_PATH = f"{run_time_path}/stack_config.json"
    with open(STACK_CONFIG_PATH, 'r') as file:
        config = json.load(file)

    global stack_config
    stack_config  = config

    return config


# For reading the server config
server_config = ConfigParser()

def read_server_config(run_time_path:str) -> None:
    """This method for reading server configs."""

    SERVER_CONFIG_PATH = f"{run_time_path}/server.conf"
    server_config.read(SERVER_CONFIG_PATH)

    return server_config


# Both config methods are called from here.
def read_configurations(run_time_path:str) -> None:
    global path
    path = run_time_path
    server_configurations = read_server_config(run_time_path)
    stack_configurations = read_stack_config(run_time_path)

    return server_configurations, stack_configurations