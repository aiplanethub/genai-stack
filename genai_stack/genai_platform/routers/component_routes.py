from typing import Dict, List, Union
from fastapi import APIRouter

from genai_stack.genai_platform.services import ComponentService
from genai_stack.genai_platform.models import (
    StackComponentRequestModel, 
    StackComponentResponseModel, 
    StackComponentFilterModel, 
    StackComponentUpdateRequestModel,
    NotFoundResponseModel,
    DeleteResponseModel,
    BadRequestResponseModel
)
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
def get_component(component_id:int) -> Union[StackComponentResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.get_component(filter)  

@router.patch("/{component_id}")
def patch_component(component_id:int, component:StackComponentUpdateRequestModel) -> Union[
    StackComponentResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.update_component(filter, component)

@router.put("/{component_id}")
def put_component(component_id:int, component:StackComponentUpdateRequestModel) -> Union[
    StackComponentResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.update_component(filter, component)

@router.delete("/{component_id}")
def delete_component(component_id:int) -> Union[DeleteResponseModel, NotFoundResponseModel]:
    filter = StackComponentFilterModel(id=component_id)
    return service.delete_component(filter)