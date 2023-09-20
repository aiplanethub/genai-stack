from fastapi import FastAPI, Response, status
from typing import Dict, List, Union

from genai_stack.genai_store.sql_store import  SQLStore
from genai_stack.genai_server.services.stack_service import StackService
from genai_stack.genai_store.sql_store import SQLDatabaseDriver
from genai_stack.genai_server.models.stack_models import StackRequestModel, StackResponseModel, StackFilterModel, StackUpdateRequestModel
from genai_stack.genai_server.models.delete_model import DeleteResponseModel
from genai_stack.genai_server.models.not_found_model import NotFoundResponseModel
from genai_stack.genai_server.models.bad_request_model import BadRequestResponseModel


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
def get_stack(stack_id:int, response:Response) -> Union[StackResponseModel, NotFoundResponseModel]:
    filter = StackFilterModel(id=stack_id)
    return service.get_stack(filter, response)  

@app.delete("/api/stack/{stack_id}")
def delete_stack(stack_id:int, response:Response) -> Union[DeleteResponseModel, NotFoundResponseModel]:
    filter = StackFilterModel(id=stack_id)
    return service.delete_stack(filter, response)   

@app.patch("/api/stack/{stack_id}")
def update_stack(stack_id:int, stack:StackUpdateRequestModel, response:Response) -> Union[
    StackResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
    filter = StackFilterModel(id=stack_id)
    return service.update_stack(filter, stack, response)