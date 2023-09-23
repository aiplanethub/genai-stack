from typing import List
from genai_stack.enums import Actions

from genai_stack.genai_store.schemas import StackSchema, StackComponentSchema
from genai_stack.genai_platform.models import StackResponseModel, StackComponentResponseModel

def check_components_list_type(components:list):
    is_primary_keys = all(isinstance(component, int) for component in components)
    if is_primary_keys:
        return Actions.GET
    else:
        return Actions.CREATE
    
def get_stack_response(stack:StackSchema, components:List[StackComponentResponseModel]) -> StackResponseModel:
    """This methods converts the StackSchema to StackResponseModel."""

    return StackResponseModel(
            id=stack.id,
            name=stack.name,
            description=stack.description,
            components=components,
            created_at=stack.created_at,
            modified_at=stack.modified_at
        )

def get_component_response(component:StackComponentSchema) -> StackComponentResponseModel:
    """This method converts the StackComponentSchema to StackComponentResponseModel."""

    return StackComponentResponseModel(
            id=component.id,
            type=component.type,
            config=component.config,
            meta_data=component.meta_data,
            created_at=component.created_at,
            modified_at=component.modified_at
        )