from genai_stack.genai_store.sql_store import SQLStore
from genai_stack.genai_platform.settings.settings import settings
from genai_stack.genai_store.schemas.base_schemas import BaseSchema

db_url = settings.CONNECTION_STRING
db_name = settings.DATABASE_NAME

def initialize_store() -> SQLStore:
    return SQLStore(url=db_url, meta_data=BaseSchema.metadata, table_name="stacks")