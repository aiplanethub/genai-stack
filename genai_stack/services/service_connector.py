from typing import Dict
from pydantic import BaseModel

from genai_stack.stack.stack_component import StackComponent
from genai_stack.stack.stack_component_config import StackComponentConfig
from genai_stack.utils.common import load_json


class BaseServiceConnectorConfigModel(BaseModel):
    config_path: str
    """ Path to the service config """


class BaseServiceConnectorConfig(StackComponentConfig):
    data_model = BaseServiceConnectorConfigModel


class BaseServiceConnector(StackComponent):
    """
    This Service Connector can mimick (duck type) an existing component so that instead of computing
    whatever we are doing in current process we make a request to a deployed component process running remotely to
    avoid loading and reloading the component.

    Note: This would make sense only if your component is memory or compute intensive such that you need to deploy
    it separately. (E.g: Embeddings and Models)
    """

    config_class = BaseServiceConnectorConfig

    def _post_init(self):
        self.service_config = load_json(self.config.config_path)
