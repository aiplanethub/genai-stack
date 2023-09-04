from typing import Optional, Union

from weaviate import EmbeddedOptions
from weaviate.auth import AuthCredentials
from weaviate.client import TIMEOUT_TYPE
from weaviate.config import Config

from genai_stack.vectordb.base import BaseVectorDBConfig, BaseVectorDBConfigModel

class WeaviateDBConfigModel(BaseVectorDBConfigModel):
    url: Optional[str] = None
    auth_client_secret: Optional[AuthCredentials] = None
    timeout_config: TIMEOUT_TYPE = (10, 60)
    proxies: Union[dict, str, None] = None
    trust_env: bool = False
    additional_headers: Optional[dict] = None
    startup_period: Optional[int] = 5
    embedded_options: Optional[EmbeddedOptions] = None
    additional_config: Optional[Config] = None


class WeaviateDBConfig(BaseVectorDBConfig):
    data_model = WeaviateDBConfigModel
