from fastapi import HTTPException
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
    DeleteResponseModel,
    # PaginationRequestModel,
    # PaginationResponseModel
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
    

    def list_stack(self, pagination_params:dict) -> dict:
        """This method returns the list of stack."""

        with Session(self.engine) as session:
            stacks = session.query(StackSchema).all()

            results:List[StackResponseModel] = []

            # Initializing the component service to create or get the components.
            component_service = ComponentService(store=self.store)

            for stack in stacks:
                compositions = session.query(StackCompositionSchema)\
                    .filter(StackCompositionSchema.stack_id == stack.id).all()
                
                components:List[StackComponentResponseModel] = []

                for composition in compositions:
                    filter = StackComponentFilterModel(id=composition.component_id)
                    component = component_service.get_component(filter)
                    components.append(component)
                
                result = get_stack_response(stack, components)
                results.append(result)

            pagination_params["results"] = results
            pagination_params["endpoint"] = "stack"

            return self.pagination(pagination_params)

    def get_stack(self, filter:StackFilterModel) -> Union[StackResponseModel, NotFoundResponseModel]:
        """This method returns the existing stack."""

        with Session(self.engine) as session:
            stack = session.get(StackSchema, filter.id)

            if stack is None:
                raise HTTPException(status_code=404, detail=f"Stack with id {filter.id} does not exist.")
            
            # Populating components related to stack will be improved.
            compositions = session.query(StackCompositionSchema).filter(StackCompositionSchema.stack_id == stack.id)

            # Initializing the component service to get the components.
            component_service = ComponentService(store=self.store)

            components:List[StackComponentResponseModel] = []

            for composition in compositions:
                filter = StackComponentFilterModel(id=composition.component_id)
                component = component_service.get_component(filter)
                components.append(component)

            return get_stack_response(stack, components)

    def update_stack(self, filter:StackFilterModel, stack:StackUpdateRequestModel) -> Union[
            StackResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
        """This method updates the existing stack."""
        
        with Session(self.engine) as session:
            old_stack = session.get(StackSchema, filter.id)

            if old_stack is None:
                raise HTTPException(status_code=404, detail=f"Stack with id {filter.id} does not exist.")
            
            if stack.name == None and stack.description == None and stack.components == None:    
                raise HTTPException(status_code=400, detail="Please provide data to update the stack.")

            components:List[StackComponentResponseModel] = []

            # Initializing the component service to create or get the components.
            component_service = ComponentService(store=self.store)

            if stack.components is not None:
                if len(stack.components) == 0:
                    raise HTTPException(
                        status_code=400, 
                        detail="""Please provide list of Components primary keys or objects containing the required fields to 
                        create new components and to update the stack."""
                    )
                else:
                    # Checking whether List containing a integers(Primary keys of already created components) or 
                    # Objects(To create new components).
                    list_type = check_components_list_type(stack.components)

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

                    # Deleting old compositions this current stack has.
                    compositions = session.query(StackCompositionSchema).filter(StackCompositionSchema.stack_id == old_stack.id)
                    for composition in compositions:
                        session.delete(composition)
                        session.commit()

                    # Creating new composition between stack and the newly retrieved or created components
                    for component in components:
                        composition = StackCompositionSchema(stack_id=old_stack.id, component_id=component.id)
                        session.add(composition)
                        session.commit()
            else:
                compositions = session.query(StackCompositionSchema).filter(StackCompositionSchema.stack_id == old_stack.id)
                for composition in compositions:
                    filter = StackComponentFilterModel(id=composition.component_id)
                    component = component_service.get_component(filter)
                    components.append(component)
            
            if stack.name is not None:
                old_stack.name = stack.name

            if stack.description is not None:
                old_stack.description = stack.description

            session.commit()

            return get_stack_response(old_stack, components)

    def delete_stack(self, filter:StackFilterModel) -> Union[DeleteResponseModel, NotFoundResponseModel]:
        """This method deletes the existing stack."""
    
        with Session(self.engine) as session:
            stack = session.get(StackSchema, filter.id)
        
            if stack is None:
                raise HTTPException(status_code=404, detail=f"Stack with id {filter.id} does not exist.")
            
            # Deleting old compositions this current stack has.
            # CASCADE is not working, this step will be removed once we find out the solution.
            compositions = session.query(StackCompositionSchema).filter(StackCompositionSchema.stack_id == stack.id)
            for composition in compositions:
                session.delete(composition)
                session.commit()
        
            session.delete(stack)
            session.commit()

            return DeleteResponseModel(detail=f"Successfully deleted {stack.name} stack.")