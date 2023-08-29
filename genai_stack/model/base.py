# import json
from typing import Any, Optional
from pydantic import BaseModel as PydanticBaseModel

# import torch
# from langchain.memory import VectorStoreRetrieverMemory
# from langchain.schema import Document

from genai_stack.core import BaseComponent, ConfigLoader
from genai_stack.constants.model import MODEL_CONFIG_KEY

# from genai_stack.model.server import HttpServer
from genai_stack.retriever import BaseRetriever
from genai_stack.utils.defaults import get_default_retriever

# from genai_stack.etl.lang_loader import LangLoaderEtl
# from genai_stack.etl.utils import get_config_from_source_kwargs

from genai_stack.stack.stack_component import StackComponent, StackComponentConfig


class BaseModelConfigModel(PydanticBaseModel):
    """
    Data Model for the configs
    """

    pass


class BaseModelConfig(StackComponentConfig):
    data_model = BaseModelConfigModel


class BaseModel(StackComponent):
    config_class = BaseModelConfig

    def _post_init(self, *args, **kwargs):
        self.model = self.load()

    def load(self):
        raise NotImplementedError

    def predict(self, query: Any):
        raise NotImplementedError

    def parameters(self):
        pass


# class BasedModel(BaseComponent, HttpServer):
#     module_name = "Model"
#     config_key = MODEL_CONFIG_KEY

#     def __init__(
#         self,
#         config: str = None,
#         model_path: Optional[str] = None,
#         retriever: BaseRetriever = None,
#     ):
#         if config:
#             ConfigLoader.__init__(self, self.module_name, config=config)
#             self.parse_config(self.config_key, getattr(self, "required_fields", None))
#         self.load(model_path=model_path)
#         if not retriever:
#             self.retriever = get_default_retriever()
#         else:
#             self.retriever = retriever

#     def get_vector_query(self, query_type: str = "similarity"):
#         pass

#     def preprocess(self, query: str):
#         if isinstance(query, bytes):
#             return query.decode("utf-8")
#         return query

#     def get_memory(self):
#         return VectorStoreRetrieverMemory(
#             retriever=self.retriever.get_langchain_memory_retriever(),
#             memory_key="chat_history",
#             input_key="question",
#         )

#     def chat_history(self):
#         chat_history = VectorStoreRetrieverMemory(
#             retriever=self.retriever.get_langchain_memory_retriever(), memory_key="chat_history", return_docs=True
#         ).load_memory_variables({"question": "question"})
#         return self._jsonify(self._parse_source_documents(chat_history["chat_history"], flatten=True))

#     def load(self, model_path: str):
#         self.model = model_path

#     def predict(self, query: Any):
#         raise NotImplementedError

#     def get_device(self):
#         return torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

#     def add_source(self, source_type: str, source: dict):
#         vectordb = self.retriever.vectordb

#         etl = LangLoaderEtl(
#             config=get_config_from_source_kwargs(source_type=source_type, source=source), vectordb=vectordb
#         )
#         print("Storing everything to vectordb")
#         etl.run()
#         print("ETL Process completed")

#     def _jsonify(self, result: dict) -> str:
#         return json.dumps(result)

#     def _parse_source_documents(self, source_documents: List[Document], flatten=False):
#         documents = [
#             {
#                 "content": document.page_content,
#                 "metadata": document.metadata,
#             }
#             for document in source_documents
#         ]

#         if flatten:
#             content_strings = [doc["content"] for doc in documents]
#             documents = {"result": "".join(content_strings)}
#         return documents
