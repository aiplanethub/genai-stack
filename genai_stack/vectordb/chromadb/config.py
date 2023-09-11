from typing import Optional
from pydantic import Field, BaseModel


from genai_stack.vectordb.base import BaseVectorDBConfig, BaseVectorDBConfigModel
from genai_stack.vectordb.constants import SearchMethod


class ChromaDBConfigModel(BaseModel):
    host: Optional[str] = None
    port: Optional[int] = None
    persist_path: Optional[str] = None
    search_method: Optional[SearchMethod] = SearchMethod.SIMILARITY_SEARCH
    search_options: Optional[dict] = Field(default_factory=dict)


class ChromaDBConfig(BaseVectorDBConfig):
    data_model = ChromaDBConfigModel
