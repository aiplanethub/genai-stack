from fastapi import FastAPI, Response, status
from typing import Dict, List, Union

from genai_stack.genai_store.sql_store import  SQLStore
from genai_stack.genai_server.services.stack_service import StackService
from genai_stack.genai_store.sql_store import SQLDatabaseDriver
from genai_stack.genai_server.models.stack_models import StackRequestModel, StackResponseModel, StackFilterModel
from genai_stack.genai_server.models.delete_model import DeleteResponseModel


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

@app.get("/api/stack/{stack_id}") 
def get_stack(stack_id:int, response:Response) -> Union[StackResponseModel, Dict[str, str]]:
    filter = StackFilterModel(id=stack_id)
    stack = service.get_stack(filter)

    if stack is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail":"Stack not found."}
    
    return stack

@app.delete("/api/stack/{stack_id}")
def get_stack(stack_id:int) -> DeleteResponseModel:
    filter = StackFilterModel(id=stack_id)
    return service.delete_stack(filter)

# @app.patch("/api/stack/{stack_id}")
# def update_stack(stack:StackPatchModel,stack_id:int):
#     print(stack,stack_id)