from genai_stack.genai_store.sql_store import SQLStore
# from genai_stack.genai_platform.models import PaginationRequestModel, PaginationResponseModel

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
    
    def pagination(self, pagination_params:dict) -> dict:
        
        page = pagination_params.get("page")
        limit = pagination_params.get("limit")
        results = pagination_params.get("results")
        endpoint = pagination_params.get("endpoint")

        next = "http://127.0.0.1:8000/api/{endpoint}?page={page}&limit={limit}"
        prev = "http://127.0.0.1:8000/api/{endpoint}?page={page}&limit={limit}"

        start_index = (page - 1) * limit
        end_index = page * limit

        total_items = len(results)

        if start_index > 0:
            prev = prev.format(endpoint=endpoint, page=page-1, limit=limit)
        else:
            prev = None
        
        if end_index < total_items:
            next = next.format(endpoint=endpoint, page=page+1, limit=limit)
        else:
            next = None

        results_list = []
        if total_items != 0:
            results_list = results[start_index:end_index]

        return {
            "total":total_items,
            "prev":prev,
            "next":next,
            "results":results_list
        }