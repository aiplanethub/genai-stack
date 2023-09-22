from fastapi import Response, status
from typing import List, Dict, Union
from sqlalchemy.orm import Session

from genai_stack.genai_platform.services import BaseService
from genai_stack.genai_platform.models import (
    StackComponentRequestModel, 
    StackComponentResponseModel, 
    StackComponentFilterModel, 
    StackComponentUpdateRequestModel,
    NotFoundResponseModel,
    BadRequestResponseModel,
    DeleteResponseModel
)
from genai_stack.genai_store.schemas import StackComponentSchema


class ComponentService(BaseService):

    def create_component(self, component:StackComponentRequestModel) -> StackComponentResponseModel:
        """This method create a new component."""
        
        with Session(self.engine) as session:
            new_component = StackComponentSchema(**{k:v for k,v in component})
            session.add(new_component)
            session.commit()

            response = StackComponentResponseModel(
                id=new_component.id,
                type=new_component.type,
                config=new_component.config,
                meta_data=new_component.meta_data,
                created_at=new_component.created_at,
                modified_at=new_component.modified_at
            )
            return response
    

    def list_components(self) -> Dict[str,List[StackComponentResponseModel]]:
        """This method returns the list of components."""

        with Session(self.engine) as session:
            components = session.query(StackComponentSchema).all()

            response = {
                "components":[]
            }

            for component in components:
                response['components'].append(StackComponentResponseModel(
                    id=component.id,
                    type=component.type,
                    config=component.config,
                    meta_data=component.meta_data,
                    created_at=component.created_at,
                    modified_at=component.modified_at
                ))
            return response

    def get_component(self, filter:StackComponentFilterModel, response:Response) -> Union[StackComponentResponseModel, NotFoundResponseModel]:
        """This method returns the existing component."""

        with Session(self.engine) as session:
            component = session.query(StackComponentSchema)\
            .filter(StackComponentSchema.id == filter.id)\
            .first()

            if component is None:
                response.status_code = status.HTTP_404_NOT_FOUND
                return NotFoundResponseModel(detail=f"Component with id {filter.id} does not exist.")

            response_dict = StackComponentResponseModel(
                id=component.id,
                type=component.type,
                config=component.config,
                meta_data=component.meta_data,
                created_at=component.created_at,
                modified_at=component.modified_at
            )
            return response_dict

    def update_component(self, filter:StackComponentFilterModel, component:StackComponentUpdateRequestModel, response:Response) -> Union[
            StackComponentResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
        """This method updates the existing component."""
        
        with Session(self.engine) as session:
            old_component = session.get(StackComponentSchema, filter.id)

            if old_component is None:
                response.status_code = status.HTTP_404_NOT_FOUND
                return NotFoundResponseModel(detail=f"Component with id {filter.id} does not exist.")
            
            if component.type == None and component.config == None and component.meta_data == None:    
                response.status_code = status.HTTP_400_BAD_REQUEST
                return BadRequestResponseModel(detail="Please provide data to update the component.")

            if component.type is not None:
                old_component.type = component.type

            if component.config is not None:
                old_component.config = component.config
            
            if component.meta_data is not None:
                old_component.meta_data = component.meta_data

            session.commit()

            response_dict = StackComponentResponseModel(
                id=old_component.id,
                type=old_component.type,
                config=old_component.config,
                meta_data=old_component.meta_data,
                created_at=old_component.created_at,
                modified_at=old_component.modified_at
            )

            return response_dict

    def delete_component(self, filter:StackComponentFilterModel, response:Response) -> Union[DeleteResponseModel, NotFoundResponseModel]:
        """This method deletes the existing component."""
    
        with Session(self.engine) as session:
            component = session.get(StackComponentSchema, filter.id)
        
            if component is None:
                response.status_code = status.HTTP_404_NOT_FOUND
                return NotFoundResponseModel(detail=f"Component with id {filter.id} does not exist.")
        
            session.delete(component)
            session.commit()

            return DeleteResponseModel(detail=f"Successfully deleted {component.type} component.")