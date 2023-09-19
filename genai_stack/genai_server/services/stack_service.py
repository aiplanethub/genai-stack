from typing import List
from sqlalchemy.orm import Session

from genai_stack.genai_server.services.base_service import BaseService
from genai_stack.genai_server.models.stack_models import StackRequestModel, StackResponseModel, StackFilterModel
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
    

    def list_stack(self, filters:StackFilterModel) -> List[StackResponseModel]:
        """This method returns the list of stack."""
        pass

    def get_stack(self, filters:StackFilterModel) -> StackResponseModel:
        """This method returns the existing stack."""
        pass

    def update_stack(self) -> StackResponseModel:
        """This method updates the existing stack."""
        pass

    def delete_stack(self):
        """This method deletes the existing stack."""
        pass