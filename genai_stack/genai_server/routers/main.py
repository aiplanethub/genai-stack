from fastapi import FastAPI
from typing import Dict, List

from genai_stack.genai_store.sql_store import  SQLStore
from genai_stack.genai_server.services.stack_service import StackService
from genai_stack.genai_store.sql_store import SQLDatabaseDriver
from genai_stack.genai_server.models.stack_models import StackRequestModel, StackResponseModel


store = SQLStore(
    url=f"sqlite:////Users/sunil/Documents/aiplanet/genai/genai-stack/db", 
    driver=SQLDatabaseDriver.SQLITE, 
    database="db"
)

service = StackService(store=store)

app = FastAPI()

@app.post('/api/stack')
def create_stack(stack:StackRequestModel) -> StackResponseModel:
    return service.create_stack(stack=stack)

@app.get("/api/stack")
def list_stack() -> Dict[str, List[StackResponseModel]]:
    return service.list_stack()