from fastapi import Response, status
from typing import List, Dict, Union
from sqlalchemy.orm import Session

from genai_stack.genai_server.services.base_service import BaseService
from genai_stack.genai_server.models.stack_models import StackRequestModel, StackResponseModel, StackFilterModel
from genai_stack.genai_server.models.delete_model import DeleteResponseModel
from genai_stack.genai_server.models.not_found_model import NotFoundResponseModel
from genai_stack.genai_store.schemas.stack_schemas import StackSchema

class StackService(BaseService):

    def create_stack(self, stack:StackRequestModel) -> StackResponseModel:
        """This method create a new stack."""
        
        with Session(self.engine) as session:
            new_stack = StackSchema(name=stack.name, description=stack.description)
            session.add(new_stack)
            session.commit()

            response = StackResponseModel(
                id=new_stack.id,
                name=new_stack.name,
                description=new_stack.description,
                components=new_stack.components,
                created_at=new_stack.created_at,
                modified_at=new_stack.modified_at
            )
            return response
    

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

            response = StackResponseModel(
                id=stack.id,
                name=stack.name,
                description=stack.description,
                components=stack.components,
                created_at=stack.created_at,
                modified_at=stack.modified_at
            )
            return response

    def update_stack(self) -> StackResponseModel:
        """This method updates the existing stack."""
        pass

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