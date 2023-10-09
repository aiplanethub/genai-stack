import tempfile
import os
import warnings
from typing import List

from langchain.vectorstores import Chroma as LangChainChroma

from genai_stack.utils.extraction import extract_class_init_attrs
from genai_stack.vectordb.base import BaseVectorDB
from genai_stack.vectordb.chromadb import ChromaDBConfig, ChromaDBConfigModel
from genai_stack.utils.sanitize import sanitize_params_dict
from genai_stack.vectordb.utils import HybridSearchResponse

try:
    import chromadb
except RuntimeError:
    """
    Chromadb's main sql engine is sqlite3 but in some distributions and platforms sqlite3 binary is not
    identified correctly.
    So incase we cannot import chromadb correctly due to this import issue we install pysqlite3 binary and swap
    the system path to use the installed binary instead of searching for the default sqlite3 binary
    """
    from genai_stack.vectordb.utils import use_pysqlite3

    use_pysqlite3()
    import chromadb


class ChromaDB(BaseVectorDB):
    config_class = ChromaDBConfig
    _client: chromadb.Client = None

    def _post_init(self, *args, **kwargs):
        db_parameters: ChromaDBConfigModel = self.config.config_data

        # Create a chromadb client
        if db_parameters.host and db_parameters.port:
            self.client = chromadb.HttpClient(host=db_parameters.host, port=db_parameters.port)
        else:
            self.client = chromadb.PersistentClient(db_parameters.persist_path or self._get_default_persistent_path())

    def _get_default_persistent_path(self):
        return os.path.join(tempfile.gettempdir(), "genai_stack")

    @property
    def client(self) -> chromadb.Client:
        return self._client

    @client.setter
    def client(self, db_client: chromadb.Client):
        self._client = db_client

    @property
    def lc_client(self):
        # Get params to be passed for initialization based on the params provided by user
        init_params = extract_class_init_attrs(LangChainChroma)
        sanitized_init_params = sanitize_params_dict(
            init_params,
            dict(self.config.config_data),
        )

        return self._create_langchain_client(**sanitized_init_params)

    def _create_langchain_client(self, **kwargs):
        if self.config.config_data.index_name:
            kwargs["collection_name"] = self.config.config_data.index_name
        return LangChainChroma(
            client=self.client,
            embedding_function=self.mediator.get_embedding_function(),
            **kwargs
        )

    def hybrid_search(
        self,
        query: str,
        metadata: dict = None,
        k: int = 1,
        **kwargs,
    ) -> List[HybridSearchResponse]:
        client = self._create_langchain_client(collection_name=kwargs.get("index_name"))
        args = {
            "query": query,
            "k": k
        }
        if metadata:
            args["filter"] = metadata
            if len(metadata.keys()) > 1:
                warnings.warn("Multiple metadata keys are not supported in ChromaDB. Only the first metadata key will be used.")
                first_most_metadata = list(metadata.keys())[0]
                args["filter"] = {first_most_metadata: metadata[first_most_metadata]}
        documents = client.similarity_search_with_score(**args)
        return [HybridSearchResponse(
            query=document[0].page_content,
            metadata=document[0].metadata if document[0].metadata else None,
            score=document[1],
            isSimilar=document[1] < 0.10,
            document=document[0]
        ) for document in documents]

    def create_index(self, index_name: str, **kwargs):
        return self._create_langchain_client(collection_name=index_name)
