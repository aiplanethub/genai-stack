from typing import Any, Callable

from langchain.vectorstores import Chroma as LangChainChroma

from genai_stack.utils.extraction import extract_class_init_attrs
from genai_stack.vectordb.base import BaseVectorDB
from genai_stack.vectordb.chromadb import ChromaDBConfig, ChromaDBConfigModel
from genai_stack.vectordb.chromadb.constants import DEFAULT_SEARCH_OPTIONS

try:
    import chromadb
except RuntimeError:
    from genai_stack.vectordb.utils import use_pysqlite3

    use_pysqlite3()
    import chromadb


class ChromaDB(BaseVectorDB):
    config_class = ChromaDBConfig
    _client: chromadb.Client = None

    def _sanitize_params_dict(self, params_dict, source_dict):
        sanitized_dict = {}
        params_dict.pop("args", None)
        params_dict.pop("kwargs", None)
        for key, val in params_dict.items():
            param_val = source_dict.get("fields", {}).get(key)
            if val and param_val or not val:
                sanitized_dict[key] = param_val
        return sanitized_dict

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
        sanitized_init_params = self._sanitize_params_dict(
            init_params,
            self.search_options,
        )

        self.lc_chroma = LangChainChroma(
            client=self.client,
            **sanitized_init_params,
        )

    @property
    def client(self) -> chromadb.Client:
        return self._client

    @client.setter
    def client(self, db_client: chromadb.Client):
        self._client = db_client

    def search_method(self, query: str):
        search_methods = {"similarity_search": self.similarity_search, "max_marginal_relevance_search": self.mmr}
        self._search_method = search_methods.get(self.config.search_method)(query=query)

    def similarity_search(self, query: str):
        return self.lc_chroma.similarity_search(
            query=query,
            **self.search_options,
        )

    def mmr(self, query: str):
        return self.lc_chroma.max_marginal_relevance_search(query=query, **self.search_options)

    def search(self, query: Any):
        return self.search_method(query)


# # Usage 1
# chroma_db = ChromaDB.from_kwargs(...)
# chroma_db.query(...)

# # Usage 2
# chroma_db = ChromaDB(config_class=ChromaDBConfig())
