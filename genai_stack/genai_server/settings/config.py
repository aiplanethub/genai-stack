import json


# Storing the runtime path
path:str = ""


# For reading stack config
stack_config = {}

def read_stack_config(run_time_path:str):
    """This method for reading stack configs."""

    path = run_time_path

    STACK_CONFIG_PATH = f"{run_time_path}/stack_config.json"
    with open(STACK_CONFIG_PATH, 'r') as file:
        stack_config = json.load(file)
        return stack_config

