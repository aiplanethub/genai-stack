from typing import Any, Optional, List

from llaim.model.server import HttpServer
from llaim.retriever import BaseRetriever
from llaim.constants.model import MODEL_CONFIG_KEY
from llaim.config import ConfigLoader


class BaseModel(HttpServer, ConfigLoader):
    module_name = "Model"
    config_key = MODEL_CONFIG_KEY

    def __init__(self, config: str = None, model_path: Optional[str] = None, retriever: BaseRetriever = None):
        super(ConfigLoader, self).__init__(name="Model", config=config)
        self.load(model_path=model_path)
        self.retriever = retriever
        self.parse_config(self.config_key, self.compulsory_fields)

    def get_vector_query(self, query_type: str = "similarity"):
        pass

    def load(self, model_path: str):
        self.model = model_path

    def predict(self, query: Any):
        raise NotImplementedError
