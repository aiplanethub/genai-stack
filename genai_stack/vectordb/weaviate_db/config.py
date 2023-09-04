from typing import Optional, Union

from weaviate.auth import AuthCredentials


from genai_stack.vectordb.base import BaseVectorDBConfig, BaseVectorDBConfigModel


class WeaviateDBConfigModel(BaseVectorDBConfigModel):
    url: str
    text_key: str
    index_name: str
    auth_client_secret: Optional[AuthCredentials] = None
    timeout_config: Optional[tuple] = (10, 60)
    additional_headers: Optional[dict] = None
    startup_period: Optional[int] = 5


class WeaviateDBConfig(BaseVectorDBConfig):
    data_model = WeaviateDBConfigModel
