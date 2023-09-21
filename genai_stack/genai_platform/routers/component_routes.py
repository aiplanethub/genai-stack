from typing import Dict, List, Union
from fastapi import APIRouter, Response

from genai_stack.genai_platform.services.component_service import ComponentService
from genai_stack.genai_platform.models.component_models import (
    StackComponentRequestModel, 
    StackComponentResponseModel, 
    StackComponentFilterModel, 
    StackComponentUpdateRequestModel
)
from genai_stack.genai_platform.models.not_found_model import NotFoundResponseModel
from genai_stack.genai_platform.models.delete_model import DeleteResponseModel
from genai_stack.genai_platform.models.bad_request_model import BadRequestResponseModel
from genai_stack.genai_platform.database import initialize_store
from genai_stack.constant import API, COMPONENT


store = initialize_store()

service = ComponentService(store=store)

router = APIRouter(
    prefix= API + COMPONENT,
    tags=['component']
)

@router.post('')
def create_component(component:StackComponentRequestModel) ->  StackComponentResponseModel:
    return service.create_component(component)

@router.get('')
def list_components() -> Dict[str, List[StackComponentResponseModel]]:
    return service.list_components()

@router.get("/{component_id}") 
def get_component(component_id:int, response:Response) -> Union[StackComponentResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.get_component(filter, response)  

@router.patch("/{component_id}")
def patch_component(component_id:int, component:StackComponentUpdateRequestModel, response:Response) -> Union[
    StackComponentResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.update_component(filter, component, response)

@router.put("/{component_id}")
def put_component(component_id:int, component:StackComponentUpdateRequestModel, response:Response) -> Union[
    StackComponentResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.update_component(filter, component, response)

@router.delete("/{component_id}")
def delete_component(component_id:int, response:Response) -> Union[DeleteResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.delete_component(filter, response)