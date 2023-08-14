from typing import Any, Dict, List

from langchain import document_loaders
from langchain.docstore.document import Document as LangDocument
import logging

from llm_stack.etl.base import EtlBase
from llm_stack.core import BaseComponent
from llm_stack.vectordb.base import BaseVectordb
from llm_stack.utils.importing import import_class
from llm_stack.constants.vectordb import VECTORDB_CONFIG_KEY

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


class LangLoaderEtl(BaseComponent):
    def __init__(
        self,
        config: str,
        name: str = "LangLoaderEtl",
        vectordb: BaseVectordb = None,
    ) -> None:
        self.vectordb = vectordb
        super().__init__(name=name, config=config)

    def load_from_source(self):
        source = self.config.get("source")
        LoaderCls = import_class(
            f"langchain.document_loaders.{source.get('name')}",
        )
        loader = LoaderCls(**source.get("fields"))
        self.documents = loader.load()
        return self.documents

    def load_into_destination(self, source_docs: List[LangDocument]):
        self.vectordb.store_documents(source_docs)
        logger.info("Stored to vectordb")

    def run(self):
        source_docs: List[LangDocument] = self.load_from_source()
        self.load_into_destination(source_docs=source_docs)
