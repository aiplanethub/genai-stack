from typing import Any, Optional
from llaim.model.server import HttpServer

from retrieval import BaseRetriever

class BaseModel(HttpServer):
    def __init__(
        self,
        name: str = None,
        model_path: Optional[str] = None,
        vector_store: Optional[Any] = None,
    ):
        self.vector_store = vector_store
        self.load(model_path=model_path)

    def get_vector_query(self, query_type: str = "similarity"):
        pass

    def load(self, model_path: str):
        self.model = model_path

    def predict(self, query: Any):
        raise NotImplementedError
