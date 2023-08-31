from typing import Any, Dict, List, Union
from pydantic import BaseModel
import logging

from langchain import document_loaders
from langchain.docstore.document import Document as LangDocument

from genai_stack.utils.importing import import_class

from .base import BaseETL, BaseETLConfig, BaseETLConfigModel

logger = logging.getLogger(__name__)

documentloaders_type_to_cls_dict: Dict[str, Any] = {
    documentloader_name: import_class(
        f"langchain.document_loaders.{documentloader_name}",
    )
    for documentloader_name in document_loaders.__all__
}


def list_langchain_loaders():
    return list(
        {documentloader.__name__ for documentloader in documentloaders_type_to_cls_dict.values()}  # noqa: E501
    )


class LangchainETLConfigModel(BaseETLConfigModel):
    name: str
    fields: dict


class LangchainETLConfig(BaseETLConfig):
    data_model = LangchainETLConfigModel


class LangchainETLDocument(BaseModel):
    document: LangDocument
    embedding: List[float]
    """To store the reference to the embeddings as well in the document"""


class LangchainETL(BaseETL):
    def extract(self):
        LoaderCls = import_class(
            f"langchain.document_loaders.{self.config.name}",
        )
        loader = LoaderCls(**self.config.fields)
        self.documents = loader.load()
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
