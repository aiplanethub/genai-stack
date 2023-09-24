from fastapi import APIRouter
from typing import Dict, Union

from genai_stack.constant import API, STACK
from genai_stack.genai_platform.services import StackService
from genai_stack.genai_platform.models import (
    StackRequestModel, 
    StackResponseModel, 
    StackFilterModel, 
    StackUpdateRequestModel,
    NotFoundResponseModel,
    BadRequestResponseModel,
    DeleteResponseModel
)
from genai_stack.genai_platform.database import initialize_store


store = initialize_store()

service = StackService(store=store)

router = APIRouter(
    prefix=API + STACK,
    tags=['stack']
)

@router.post("")
def create_stack(stack:StackRequestModel) -> StackResponseModel:
    return service.create_stack(stack=stack)

@router.get("")
def list_stack(page:int = 1, limit:int = 10) -> Dict:
    pagination_params = {"page":page,"limit":limit}
    return service.list_stack(pagination_params)

@router.get("/{stack_id}") 
def get_stack(stack_id:int) -> Union[StackResponseModel, NotFoundResponseModel]:
    filter = StackFilterModel(id=stack_id)
    return service.get_stack(filter)  

@router.delete("/{stack_id}")
def delete_stack(stack_id:int) -> Union[DeleteResponseModel, NotFoundResponseModel]:
    filter = StackFilterModel(id=stack_id)
    return service.delete_stack(filter)   

@router.patch("/{stack_id}")
def update_stack(stack_id:int, stack:StackUpdateRequestModel) -> Union[
    StackResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
    filter = StackFilterModel(id=stack_id)
    return service.update_stack(filter, stack)