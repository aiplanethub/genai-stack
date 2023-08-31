from typing import Optional

from genai_stack.vectordb.base import BaseVectorDBConfig, BaseVectorDBConfigModel


class ChromaDBConfigModel(BaseVectorDBConfigModel):
    host: Optional[str]
    port: Optional[int]
    persist_path: Optional[str]


class ChromaDBConfig(BaseVectorDBConfig):
    data_model = ChromaDBConfigModel
