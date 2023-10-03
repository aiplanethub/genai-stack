from pydantic import BaseModel
from uuid import UUID
from typing import List, Union

from genai_stack.stack.stack import Stack
from genai_stack.etl.base import BaseETL
from genai_stack.embedding.base import BaseEmbedding
from genai_stack.vectordb.base import BaseVectorDB


class BaseETLPlatformConfig(BaseModel):
    pass


class BaseETLPlatform:
    """
    ETL Platform is an interface that would run the ETL processes on workflow management to enable to scale the ETL workloads more efficiently.
    """

    def __init__(
        self,
        platform_config: BaseETLPlatformConfig,
        loaders: List[BaseETL],
        embedding: BaseEmbedding,
        vectordb: BaseVectorDB,
    ):
        self.platform_config = platform_config
        self._loaders = loaders
        self._embedding = embedding
        self._vectordb = vectordb
        self.setup()

    @property
    def loaders(self):
        return self._loaders

    @property
    def embedding(self):
        return self._embedding

    @property
    def vectordb(self):
        return self._vectordb

    def get_loader_by_id(self, id: Union[str, UUID]):
        for loader in self.loaders:
            if loader.config.id == str(id):
                return loader

        raise ValueError(f"Loader with id {id} not found.")

    def setup(self):
        """
        Setup method to setup all the related things required to run the ETLPlatform
        """
        pass

    def handle_job(self, **kwargs):
        """
        A handler for incoming ETL jobs
        """
        raise NotImplementedError()
