from fastapi import FastAPI

from genai_stack.genai_store.sql_store import  SQLStore
from genai_stack.genai_store.sql_store import SQLDatabaseDriver
from genai_stack.genai_server.routers import stack_routes

store = SQLStore(
    url=f"sqlite:////Users/sunil/Documents/aiplanet/genai/genai-stack/db", 
    driver=SQLDatabaseDriver.SQLITE, 
    database="db"
)

app = FastAPI()

"""Add middleware if required."""
# app.middleware()

# to run this file locally, execute:
# uvicorn genai_stack.genai_server.genai_stack_server:app --reload

"""Connecting all the routers to app."""
app.include_router(stack_routes.router)

    


