from genai_stack.genai_store.sql_store import SQLStore
from genai_stack.genai_server.settings.settings import settings

db_url = settings.DATABASE_URI
db_name = settings.DATABASE_NAME
db_driver = settings.DATABASE_DRIVER


def initialize_store() -> SQLStore:
    return SQLStore(url=db_url, driver=db_driver, database=db_name)
