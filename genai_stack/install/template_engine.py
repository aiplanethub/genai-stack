import os
import json
import jsonschema
from jinja2 import FileSystemLoader, Environment, Template


class TemplateEngine:
    def __init__(self, path: str, component: str, sub_component: str, options: dict = None, quickstart: bool = False):
        """
        Args:
            path: The base template directory where all the required templates are kept
        """
        self.path = path
        self.component = component
        self.sub_component = sub_component
        self.quickstart = quickstart
        self.full_path = os.path.join(self.path, component, self.sub_component)
        self.env = Environment(loader=FileSystemLoader(self.full_path), trim_blocks=True, lstrip_blocks=True)

        # Initialise options to quickstart options if quickstart is True
        self.options = self.parse_json(self.get_quickstart_path()) if self.quickstart else options

    def get_options_path(self):
        return os.path.join(self.full_path, "options.json")

    def get_quickstart_path(self):
        return os.path.join(self.full_path, "quickstart.json")

    @property
    def option_name(self):
        return list(self.options.keys())[0]

    def get_template(self, template_name) -> Template:
        template = self.env.get_template(template_name)
        return template

    def parse_json(self, filepath):
        with open(filepath) as f:
            json_data = json.load(f)
        return json_data

    def get_options_schema(self):
        return self.parse_json(self.get_options_path())

    def load_options(self):
        option_json = self.get_options_schema()
        option_schema = option_json[self.option_name]

        # Extract option_name
        jsonschema.validate(option_schema, self.options)

        # override default 'other' options section with the override values
        other_options = option_json.get("other", {})
        other_options.update(self.options.get("other", {}))
        self.options["other"] = other_options

        # Get the template path
        template_path = os.path.join(option_json.get("module"), option_schema["module_name"])

        return (self._flatten_options(self.options), template_path)

    def _flatten_options(self, options) -> dict:
        """
        Convert this kind of structure
        {

            <options_name1>: {
                "field1": "value",
            },
            <option_name2>: {
                "field2": "value"
            }
        }

        to {
            "field1": "value",
            "field2": "value"
        }
        """
        result = {}
        for option in options:
            option_values = options[option]
            result.update(option_values)
        return result

    def render(self):
        all_options, template_path = self.load_options()
        rendered_template = self.get_template(template_path).render(all_options)

        return rendered_template