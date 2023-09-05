from typing import Any, Callable

from langchain.vectorstores import Chroma as LangChainChroma

from genai_stack.utils.extraction import extract_class_init_attrs
from genai_stack.vectordb.base import BaseVectorDB
from genai_stack.vectordb.chromadb import ChromaDBConfig, ChromaDBConfigModel
from genai_stack.utils.sanitize import sanitize_params_dict

try:
    import chromadb
except RuntimeError:
    from genai_stack.vectordb.utils import use_pysqlite3

    use_pysqlite3()
    import chromadb


class ChromaDB(BaseVectorDB):
    config_class = ChromaDBConfig
    _client: chromadb.Client = None

    def _post_init(self, *args, **kwargs):
        db_parameters: ChromaDBConfigModel = self.config.data_model

        # Create a chromadb client
        if db_parameters.host and db_parameters.port:
            self.client = chromadb.HttpClient(host=db_parameters.host, port=db_parameters.port)
        elif db_parameters.persist_path:
            persist_path = db_parameters.persist_path
            self.client = chromadb.PersistentClient(persist_path)
        else:
            self.client = chromadb.Client()

        self.search_options = {**self.config.search_options, **kwargs}

        # Get params to be passed for initialization based on the params provided by user
        init_params = extract_class_init_attrs(LangChainChroma)
        sanitized_init_params = sanitize_params_dict(
            init_params,
            dict(self.config),
        )

        self.lc_chroma = self._create_langchain_client(**sanitized_init_params)

    @property
    def client(self) -> chromadb.Client:
        return self._client

    @client.setter
    def client(self, db_client: chromadb.Client):
        self._client = db_client

    def _create_langchain_client(self, **kwargs):
        return LangChainChroma(client=self.client, embedding_function=self.mediator.get_embedding_function(), **kwargs)

    def create_index(self, index_name: str, **kwargs):
        return self._create_langchain_client(collection_name=index_name)

    def add_texts(self, documents):
        return self.lc_chroma.add_documents(documents)

    def search_method(self, query: str):
        search_methods = {"similarity_search": self.similarity_search, "max_marginal_relevance_search": self.mmr}
        search_results = search_methods.get(self.config.search_method)(query=query)
        return search_results

    def similarity_search(self, query: str):
        return self.lc_chroma.similarity_search(
            query=query,
            **self.search_options,
        )

    def mmr(self, query: str):
        return self.lc_chroma.max_marginal_relevance_search(query=query, **self.search_options)

    def search(self, query: Any):
        return self.search_method(query)
