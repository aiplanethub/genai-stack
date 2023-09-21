from typing import Dict, List, Union
from fastapi import FastAPI, Response

from genai_stack.genai_store.sql_store import SQLStore
from genai_stack.genai_store.sql_store import SQLDatabaseDriver
from genai_stack.genai_server.services.component_service import ComponentService
from genai_stack.genai_server.models.component_models import (
    StackComponentRequestModel, 
    StackComponentResponseModel, 
    StackComponentFilterModel, 
    StackComponentUpdateRequestModel
)
from genai_stack.genai_server.models.not_found_model import NotFoundResponseModel
from genai_stack.genai_server.models.delete_model import DeleteResponseModel
from genai_stack.genai_server.models.bad_request_model import BadRequestResponseModel


store = SQLStore(
    url=f"sqlite:////Users/sunil/Documents/aiplanet/genai/genai-stack/db", 
    driver=SQLDatabaseDriver.SQLITE, 
    database="db"
)

service = ComponentService(store=store)

app = FastAPI()

@app.post('/api/component')
def create_component(component:StackComponentRequestModel) ->  StackComponentResponseModel:
    return service.create_component(component)

@app.get("/api/component")
def list_components() -> Dict[str, List[StackComponentResponseModel]]:
    return service.list_components()

@app.get("/api/component/{component_id}") 
def get_component(component_id:int, response:Response) -> Union[StackComponentResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.get_component(filter, response)  

@app.patch("/api/component/{component_id}")
def patch_component(component_id:int, component:StackComponentUpdateRequestModel, response:Response) -> Union[
    StackComponentResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.update_component(filter, component, response)

@app.put("/api/component/{component_id}")
def put_component(component_id:int, component:StackComponentUpdateRequestModel, response:Response) -> Union[
    StackComponentResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.update_component(filter, component, response)

@app.delete("/api/component/{component_id}")
def delete_component(component_id:int, response:Response) -> Union[DeleteResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.delete_component(filter, response)