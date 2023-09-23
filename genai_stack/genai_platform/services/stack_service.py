from fastapi import HTTPException, Response, status
from typing import List, Dict, Union
from sqlalchemy.orm import Session
from genai_stack.enums import Actions

from genai_stack.genai_platform.services import BaseService
from genai_stack.genai_platform.services.component_service import ComponentService
from genai_stack.genai_platform.models import (
    StackRequestModel,
    StackResponseModel,
    StackUpdateRequestModel,
    StackFilterModel,
    StackComponentResponseModel,
    StackComponentFilterModel,
    NotFoundResponseModel,
    BadRequestResponseModel,
    DeleteResponseModel
)
from genai_stack.genai_store.schemas import StackSchema, StackCompositionSchema
from genai_stack.genai_platform.utils import check_components_list_type, get_stack_response

class StackService(BaseService):

    def create_stack(self, stack:StackRequestModel) -> StackResponseModel:
        """This method create a new stack."""
        
        with Session(self.engine) as session:

            # Checking whether components list contains the elements or not.
            if len(stack.components) == 0:
                raise HTTPException(
                    status_code=400, 
                    detail="""List of Components primary keys or objects containing the required fields to create a component 
                        are required to create a stack."""
                    )
            
            # Checking whether List containing a integers(Primary keys of already created components) or 
            # Objects(To create new components).
            list_type = check_components_list_type(stack.components)
            
            # Initializing the component service to create or get the components.
            component_service = ComponentService(store=self.store)

            components:List[StackComponentResponseModel] = []

            # Retrieving Components
            if list_type == Actions.GET:
                for component_id in stack.components:
                    filter = StackComponentFilterModel(id=component_id)
                    component = component_service.get_component(filter)
                    components.append(component)

            # Creating Components
            else:
                for component_dict in stack.components:
                    component = component_service.create_component(component_dict)
                    components.append(component)
            
            # Creating a stack
            new_stack = StackSchema(name=stack.name, description=stack.description)
            session.add(new_stack)
            session.commit()

            # Creating a composition between stack and component.
            for component in components:
                composition = StackCompositionSchema(stack_id=new_stack.id, component_id=component.id)
                session.add(composition)
                session.commit()
            
            return get_stack_response(new_stack, components)
    

    def list_stack(self) -> Dict[str,List[StackResponseModel]]:
        """This method returns the list of stack."""

        with Session(self.engine) as session:
            stacks = session.query(StackSchema).all()

            response = {
                "stacks":[]
            }

            for stack in stacks:
                response['stacks'].append(StackResponseModel(
                    id=stack.id,
                    name=stack.name,
                    description=stack.description,
                    components=stack.components,
                    created_at=stack.created_at,
                    modified_at=stack.modified_at
                ))
            return response

    def get_stack(self, filter:StackFilterModel, response:Response) -> Union[StackResponseModel, NotFoundResponseModel]:
        """This method returns the existing stack."""

        with Session(self.engine) as session:
            stack = session.query(StackSchema)\
            .filter(StackSchema.id == filter.id)\
            .first()

            if stack is None:
                response.status_code = status.HTTP_404_NOT_FOUND
                return NotFoundResponseModel(detail=f"Stack with id {filter.id} does not exist.")

            response_dict = StackResponseModel(
                id=stack.id,
                name=stack.name,
                description=stack.description,
                components=stack.components,
                created_at=stack.created_at,
                modified_at=stack.modified_at
            )
            return response_dict

    def update_stack(self, filter:StackFilterModel, stack:StackUpdateRequestModel, response:Response) -> Union[
            StackResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
        """This method updates the existing stack."""
        
        with Session(self.engine) as session:
            old_stack = session.get(StackSchema, filter.id)

            if old_stack is None:
                response.status_code = status.HTTP_404_NOT_FOUND
                return NotFoundResponseModel(detail=f"Stack with id {filter.id} does not exist.")
            
            if stack.name == None and stack.description == None:    
                response.status_code = status.HTTP_400_BAD_REQUEST
                return BadRequestResponseModel(detail="Please provide data to update the stack.")

            if stack.name is not None:
                old_stack.name = stack.name

            if stack.description is not None:
                old_stack.description = stack.description

            session.commit()

            response_dict = StackResponseModel(
                id=old_stack.id,
                name=old_stack.name,
                description=old_stack.description,
                components=old_stack.components,
                created_at=old_stack.created_at,
                modified_at=old_stack.modified_at
            )

            return response_dict

    def delete_stack(self, filter:StackFilterModel, response:Response) -> Union[DeleteResponseModel, NotFoundResponseModel]:
        """This method deletes the existing stack."""
    
        with Session(self.engine) as session:
            stack = session.get(StackSchema, filter.id)
        
            if stack is None:
                response.status_code = status.HTTP_404_NOT_FOUND
                return NotFoundResponseModel(detail=f"Stack with id {filter.id} does not exist.")
        
            session.delete(stack)
            session.commit()

            return DeleteResponseModel(detail=f"Successfully deleted {stack.name} stack.")