from genai_stack.genai_store.sql_store import SQLStore
from genai_stack.genai_store.sql_store import SQLDatabaseDriver
from genai_stack.genai_platform.settings.settings import settings

db_url = settings.CONNECTION_STRING
db_name = settings.DATABASE_NAME


def initialize_store() -> SQLStore:
    return SQLStore(url=db_url, driver=SQLDatabaseDriver.SQLITE, database=db_name)
