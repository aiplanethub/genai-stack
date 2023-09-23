from pydantic import BaseModel, Field
from typing import List, Optional, Union
from datetime import datetime

from genai_stack.genai_platform.models.component_models import StackComponentRequestModel, StackComponentResponseModel
from genai_stack.genai_platform.models.constants import STR_FIELD_MAX_LENGTH


class StackBaseModel(BaseModel):
    """Stack Base Data Model."""

    name:str = Field(
        title="The name of the stack.", 
        max_length=STR_FIELD_MAX_LENGTH
    )
    description:str = Field(
        title="The description of the stack.",
        max_length=STR_FIELD_MAX_LENGTH,
    )

class StackRequestModel(StackBaseModel):
    """
    Stack Request Data Model.
    
    Args:
        name : str
        descripiton : str
        components : List[int] | List[StackComponentRequestModel]
    
    For creating a new stack.
    """

    components:Union[List[int], List[StackComponentRequestModel]] = Field(
        title="List of Primary keys of the components that are already created or List of StackComponentRequestModel dict.",
        description="""You can create components using create component endpoint and pass a list of primary keys of created components or
          you can pass the dict containing the fields that are required to create a component."""
    )


class StackResponseModel(StackBaseModel):
    """
    Stack Response Data Model.
    
    Args:
        id : int
        name : str
        descripiton : str
        components : List[StackComponentResponseModel]
        created_at: datetime
        modified_at: Optional[datetime]

    For returning the stack data.
    """

    id:int
    name:str
    description:str
    components: List[StackComponentResponseModel]
    created_at: datetime
    modified_at: Optional[datetime] 


class StackFilterModel(BaseModel):
    """
    Stack Filter Data Model.
    
    Args:
        id : int

    For retrieving stack based on stack id.
    """

    id:int

class StackUpdateRequestModel(BaseModel):
    """
    Stack Update Request Data Model.

    Args:
        name : Optional[str]
        description : Optional[str]
        components : Optional[ List[int] | List[StackComponentRequestModel] ]
    
    For updating the exisiting stack.
    """

    name:Optional[str] = None
    description:Optional[str] = None
    components:Optional[Union[List[int], List[StackComponentRequestModel]]] = None
