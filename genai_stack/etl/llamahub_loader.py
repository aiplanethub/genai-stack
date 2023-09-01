from typing import List
from pydantic import BaseModel

from langchain.docstore.document import Document as LangDocument
from llama_index import download_loader

from genai_stack.utils.extraction import (
    extract_class_init_attrs,
    extract_method_params,
)

from .utils import LangchainETLDocument
from .base import BaseETL, BaseETLConfig, BaseETLConfigModel


class LLamaHubSource(BaseModel):
    name: str
    fields: dict


class LLamaHubETLConfigModel(BaseETLConfigModel):
    source: LLamaHubSource


class LLamaHubETLConfig(BaseETLConfig):
    data_model = LLamaHubETLConfigModel


class LLamaHubEtl(BaseETL):
    config_class = LLamaHubETLConfig

    def params_for_load_data(self, kls, method):
        return self._sanitize_params_dict(extract_method_params(kls, method))

    def params_for_class_init(self, kls):
        return self._sanitize_params_dict(extract_class_init_attrs(kls))

    def _sanitize_params_dict(self, params_dict):
        sanitized_dict = {}

        params_dict.pop("args", None)
        params_dict.pop("kwargs", None)

        for key, val in params_dict.items():
            param_val = self.config.source.fields.get(key)
            if val and param_val or not val:
                sanitized_dict[key] = param_val

        return sanitized_dict

    def extract(self):
        print("source config done")
        LoaderCls = download_loader(self.config.source.name)

        init_params = self.params_for_class_init(LoaderCls)
        load_params = self.params_for_load_data(LoaderCls, "load_data")

        loader = LoaderCls(**init_params)
        self.documents = loader.load_data(**load_params)

        # Convert struct to LangChain document format
        self.documents = [d.to_langchain_format() for d in self.documents]

        return self.documents

    def transform(self, source_docs: List[LangDocument]) -> List[LangchainETLDocument]:
        etl_documents = []
        for doc in source_docs:
            embedding = self.mediator.get_embedded_text(doc.page_content)
            etl_documents.append(LangchainETLDocument(document=doc, embedding=embedding))
        return etl_documents

    def load(self, documents: List[LangchainETLDocument]):
        for doc in documents:
            self.mediator.store_to_vectordb(data=doc.document, embedding=doc.embedding)

    def run(self):
        source_documents = self.extract()
        transformed_documents = self.transform(source_documents)
        self.load(transformed_documents)
