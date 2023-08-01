from typing import Any, Optional
from langchain.memory import VectorStoreRetrieverMemory

from llm_stack.model.server import HttpServer
from llm_stack.retriever import BaseRetriever
from llm_stack.constants.model import MODEL_CONFIG_KEY
from llm_stack.config import ConfigLoader


class BaseModel(HttpServer, ConfigLoader):
    module_name = "Model"
    config_key = MODEL_CONFIG_KEY

    def __init__(
        self,
        # config: str = None,
        model_path: Optional[str] = None,
        retriever: BaseRetriever = None,
        config_fields: dict = None,
    ):
        self.load(model_path=model_path)
        self.retriever = retriever
        self.config_fields = config_fields
        # if config:
        # ConfigLoader(self, self.module_name, config=config)
        # self.parse_config(self.config_key, getattr(self, "required_fields", None))

    def get_vector_query(self, query_type: str = "similarity"):
        pass

    def get_memory(self):
        return VectorStoreRetrieverMemory(
            retriever=self.retriever.get_langchain_memory_retriever(),
            memory_key="chat_history",
        )

    def load(self, model_path: str):
        self.model = model_path

    def predict(self, query: Any):
        raise NotImplementedError

    @classmethod
    def from_config(
        cls,
        config,
        model_path: Optional[str] = None,
        retriever: BaseRetriever = None,
    ):
        # TODO: Init a class without config file.
        # cfg = ConfigLoader(cls.module_name, config=config)
        # kls = cls(retriever, model_path)
        # kls.config_fields = cfg.parse_config(
        #     kls.config_key,
        #     getattr(kls, "required_fields", None),
        # )
        # return kls
        raise NotImplementedError
