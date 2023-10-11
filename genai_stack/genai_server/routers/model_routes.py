from fastapi import APIRouter

from genai_stack.constant import API, MODEL
from genai_stack.genai_server.settings.settings import settings
from genai_stack.genai_server.services.model_service import ModelService
from genai_stack.genai_server.models.model_models import ModelResponseModel, ModelRequestModel

service = ModelService(store=settings.STORE)

router = APIRouter(prefix=API + MODEL, tags=["model"])


@router.post("/predict")
def predict(data: ModelRequestModel) -> ModelResponseModel:
    return service.predict(data=data)
