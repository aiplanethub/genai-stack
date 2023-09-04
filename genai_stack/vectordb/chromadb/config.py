from typing import Optional
from pydantic import Field

from genai_stack.vectordb.base import BaseVectorDBConfig, BaseVectorDBConfigModel
from genai_stack.vectordb.constants import SearchMethod


class ChromaDBConfigModel(BaseVectorDBConfigModel):
    host: Optional[str]
    port: Optional[int]
    persist_path: Optional[str] = "/tmp/genaistack"
    search_method: SearchMethod = SearchMethod.SIMILARITY_SEARCH
    search_options: Optional[dict] = Field(default_factory=dict)


class ChromaDBConfig(BaseVectorDBConfig):
    data_model = ChromaDBConfigModel
