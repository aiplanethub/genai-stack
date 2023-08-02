from typing import Any, Optional


class BaseModel:
    vector_store: Optional[Any] = None

    def get_vector_query(self, query_type: str = "similarity"):
        pass

    def load(self, model_path: str):
        self.model_path = model_path

    def predict(self, query: Any):
        pass
