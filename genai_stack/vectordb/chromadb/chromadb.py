from typing import Any, Optional, Callable
from genai_stack.vectordb.base import BaseVectorDB
from genai_stack.vectordb.chromadb import ChromaDBConfig, ChromaDBConfigModel
from genai_stack.vectordb.exception import GenAIStackException
from langchain.vectorstores import Chroma as LanghChainChroma
from genai_stack.vectordb.chromadb.constants import DEFAULT_COLLECTION_NAME, DEFAULT_SEARCH_OPTIONS
from genai_stack.utils.extraction import extract_class_init_attrs

try:
    import chromadb
except RuntimeError:
    from genai_stack.vectordb.utils import use_pysqlite3

    use_pysqlite3()
    import chromadb


class ChromaDB(BaseVectorDB):
    config_class = ChromaDBConfig
    _client: chromadb.Client = None
    _search_method: Callable = None
    search_options: dict = DEFAULT_SEARCH_OPTIONS

    def _sanitize_params_dict(self, params_dict, source_dict, sanitized_dict):
        params_dict.pop("args", None)
        params_dict.pop("kwargs", None)
        for key, val in params_dict.items():
            param_val = source_dict.get("fields", {}).get(key)
            if val and param_val or not val:
                sanitized_dict[key] = param_val
        return sanitized_dict

    def _post_init(self, *args, **kwargs):
        # Create a chromadb client
        db_parameters: ChromaDBConfigModel = self.config.data_model

        if db_parameters.host and db_parameters.port:
            self.client = chromadb.HttpClient(host=db_parameters.host, port=db_parameters.port)
        elif db_parameters.persist_path:
            persist_path = db_parameters.persearch_optionssist_path
            self.client = chromadb.PersistentClient(persist_path)
        else:
            self.client = chromadb.Client()

        self.search_options = {**self.search_options, **kwargs}

        # Get params to be passed for initialization based on the params provided by user
        init_params = extract_class_init_attrs(LanghChainChroma)
        sanitized_init_params = {}
        self._sanitize_params_dict(
            init_params,
            self.search_options,
            sanitized_init_params,
        )

        self.lc_chrome = LanghChainChroma(
            client=self.client,
            **sanitized_init_params,
        )

    @property
    def search_method(self):
        return getattr(self, self._search_method)

    @search_method.setter
    def search_method(self, search_method: str = "similarity_search"):
        search_methods = {
            "similarity_search": self.similarity_search,
        }
        self._search_method = search_methods.get(search_method)

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, db_client: chromadb.Client):
        self._client = db_client

    @property
    def client(self) -> chromadb.Client:
        return

    def similarity_search(self, query: Any):
        return self.lc_chrome.similarity_search(
            query=query,
            k=self.search_options["top_k"],
        )

    def search(self, query: Any):
        return self.search_method(query)


# # Usage 1
# chroma_db = ChromaDB.from_kwargs(...)
# chroma_db.query(...)

# # Usage 2
# chroma_db = ChromaDB(config_class=ChromaDBConfig())
