from genai_stack.genai_store.sql_store import SQLStore
from genai_stack.genai_server.settings.settings import settings

db_url = settings.DATABASE_URI
meta_data = settings.META_DATA
table_name = settings.TABLE_NAME


def initialize_store() -> SQLStore:
    return SQLStore(url=db_url, meta_data=meta_data, table_name=table_name)
