from typing import Optional, Union
from pydantic import Field

from weaviate.auth import AuthCredentials
from pydantic import BaseModel
from genai_stack.vectordb.constants import SearchMethod


from genai_stack.vectordb.base import BaseVectorDBConfig, BaseVectorDBConfigModel


class WeaviateDBConfigModel(BaseModel):
    url: str
    text_key: str
    index_name: str
    auth_client_secret: Optional[AuthCredentials] = None
    timeout_config: Optional[tuple] = (10, 60)
    additional_headers: Optional[dict] = None
    startup_period: Optional[int] = 5
    search_method: Optional[SearchMethod] = SearchMethod.SIMILARITY_SEARCH
    search_options: Optional[dict] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True


class WeaviateDBConfig(BaseVectorDBConfig):
    data_model = WeaviateDBConfigModel
