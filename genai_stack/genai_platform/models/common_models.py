from pydantic import BaseModel
from typing import Optional, Union, List
from datetime import datetime

# from genai_stack.genai_platform.models.stack_models import StackResponseModel
# from genai_stack.genai_platform.models.component_models import StackComponentResponseModel

class TimeStampsModel(BaseModel):
    """Time Stamps Data Model."""

    created_at: datetime
    modified_at: Optional[datetime] 


class DetailResponseModel(BaseModel):
    """Details Response Data Model."""

    detail:str


class BadRequestResponseModel(DetailResponseModel):
    """
    Bad Request Response Data Model.

    Args:
        detail : str
    """


class NotFoundResponseModel(DetailResponseModel):
    """
    Not Found Response Data Model.

    Args:
        detail : str
    """


class DeleteResponseModel(DetailResponseModel):
    """
    Delete Response Data Model.

    Args:
        detail : str
    """

# class PaginationRequestModel(BaseModel):
#     """
#     Pagination Request Data Model.

#     Args:
#         enpoint : str
#         page : int
#         limit : int
#         results : List[StackResponseModel], List[StackComponentResponseModel], List
#     """
#     endpoint:str
#     page:int
#     limit:int
#     results:Union[List[StackResponseModel], List[StackComponentResponseModel], List]
    

# class PaginationResponseModel(BaseModel):
#     """
#     Pagination Response Data Model.

#     Args:
#         total : int,
#         prev : str | None,
#         next : next | None,
#         results : List[StackResponseModel] | List[StackComponentResponseModel] | []
#     """
#     total:int
#     prev:Union[str, None]
#     next:Union[str, None]
#     results:Union[List[StackResponseModel], List[StackComponentResponseModel], List]