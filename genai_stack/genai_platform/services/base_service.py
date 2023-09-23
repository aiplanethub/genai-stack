from genai_stack.genai_store.sql_store import SQLStore

class BaseService:
    _store : SQLStore = None

    def __init__(self, store:SQLStore) -> None:
        self._store = store

    @property
    def store(self):
        return self._store

    @property
    def engine(self):
        return self._store.engine

