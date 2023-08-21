import json
from genai_stack.constants.model import DEFAULT_MODEL_JSON


def create_default_model_json_file(config_file_name: str = "genai_stack_config.json"):
    # Serializing json
    json_object = json.dumps(DEFAULT_MODEL_JSON, indent=4)

    # Writing to sample.json
    with open(config_file_name, "w") as outfile:
        outfile.write(json_object)
    return config_file_name
