import logging
from typing import List

from langchain.docstore.document import Document as LangDocument
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
from llama_index import download_loader

from llm_stack.etl.base import EtlBase
from llm_stack.utils.extraction import (
    extract_class_init_attrs,
    extract_method_params,
)
from llm_stack.utils.importing import import_class

logger = logging.getLogger(__name__)


class LLamaHubEtl(EtlBase):
    def __init__(self, name: str = "LLamaHubEtl", config: str = None) -> None:
        super().__init__(name, config)

    def params_for_load_data(self, kls, method):
        return extract_method_params(kls, method)

    def params_for_class_init(self, kls):
        return extract_class_init_attrs(kls)

    def load_from_source(self):
        source = self.config_dict.get("source")
        print("source config done")
        LoaderCls = download_loader(source.get("name"))

        sanitized_init_params = {}
        init_params = self.params_for_class_init(LoaderCls)
        self._sanitize_params_dict(init_params, source, sanitized_init_params)

        sanitized_ld_params = {}
        ld_params = self.params_for_load_data(LoaderCls, "load_data")
        self._sanitize_params_dict(ld_params, source, sanitized_ld_params)
        loader = LoaderCls(**sanitized_init_params)
        self.documents = loader.load_data(**sanitized_ld_params)

        # Convert struct to LangChain document format
        self.documents = [d.to_langchain_format() for d in self.documents]

        return self.documents

    def _sanitize_params_dict(self, params_dict, source_dict, sanitized_dict):
        params_dict.pop("args", None)
        params_dict.pop("kwargs", None)
        for key, val in params_dict.items():
            param_val = source_dict.get("fields", {}).get(key)
            if val and param_val or not val:
                sanitized_dict[key] = param_val

    def _get_embedding(self):
        destination = self.config_dict.get("destination", {})
        if embedding := destination.get("embedding"):
            embedding_cls = import_class(
                f"langchain.embeddings.{embedding.get('name')}",
            )
            self.embedding = embedding_cls(**embedding.get("fields"))
        elif not self.embedding:
            self.embedding = OpenAIEmbeddings()
        return self.embedding

    def load_into_destination(self, source_docs: List[LangDocument]):
        destination = self.config_dict.get("destination")

        class_name = destination.get("class_name") or "llm_stack"
        class_name = class_name.capitalize()

        Weaviate.from_documents(
            source_docs,
            self._get_embedding(),
            weaviate_url=destination.get(
                "fields",
                {},
            ).get("url"),
            index_name=class_name,
        )
        logger.info("Stored to vectordb")

    def run(self):
        source_docs: List[LangDocument] = self.load_from_source()
        self.load_into_destination(source_docs=source_docs)

    def run(self):
        source_docs: List[LangDocument] = self.load_from_source()
        self.load_into_destination(source_docs=source_docs)
