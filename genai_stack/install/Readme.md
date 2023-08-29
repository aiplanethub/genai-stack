# Installation Framework

This folder mainly contains docker/docker-compose templates to install different components needed in the llm stack


# templates directory

This directory contains the templates for installation of various components needed to run the GenAI Stack. 

Each Component has its own directory under which there are lot of subcomponents

Available Components:
    Vectordb:
        * Weaviate

Each Subcomponent has a 
1. options.json and 
2. quickstart.json 

## Options.json
This json file indicates what could be the option name for the subcomponent and the jsonschema for the option. 

The "other" keyword is reserved and is used for injecting any variables into the base template itself. This field does not have any validation but comes with some preconfigured values which could be overriden.

Structure
```json
{
    "modules": "<your submodules directory containing all the child templates>",
    "<option_name>": {
        "type": "object",
        "description": "Your description for the option",
        "module_name": "<The file name of the child template>",
        "properties": {

            "<option_fields>": "<Add your jsonschema validation for this field>"
        },
        "required": ["<Mention your required fields>"]
    },

}
```

Example: genai_stack/install/templates/vectordb/weaviate/options.json


## Quickstart.json

This file contains preconfigured options for a submodule to quickstart the installation for the subcomponent

Structure
```json
{
    "<option_name>": {
        "<option_field>": "value"
    },
}
```

Example: genai_stack/install/templates/vectordb/weaviate/quickstart.json
