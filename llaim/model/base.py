from typing import Any, Optional, List
from llaim.model.server import HttpServer

from retrieval import BaseRetriever
from config import ConfigLoader


class BaseModel(HttpServer, ConfigLoader):
    module_name = "Model"
    config_key = "model"

    def __init__(
        self,
        config: str = None,
        model_path: Optional[str] = None,
        retriever: BaseRetriever = None,
    ):
        super(ConfigLoader, self).__init__(name="Model", config=config)
        self.retriever = retriever
        self.load(model_path=model_path)
        self.parse_config(self.config_key, self.compulsory_fields)

    def get_vector_query(self, query_type: str = "similarity"):
        pass

    def load(self, model_path: str):
        self.model = model_path

    def predict(self, query: Any):
        raise NotImplementedError
