from genai_stack.genai_platform.services.base_service import BaseService
from genai_stack.genai_server.models.model_models import ModelRequestModel, ModelResponseModel
from genai_stack.genai_server.utils import get_current_stack
from genai_stack.genai_server.settings.config import stack_config


class ModelService(BaseService):
    def predict(self, data: ModelRequestModel) -> ModelResponseModel:
        stack = get_current_stack(config=stack_config)
        response = stack.model.predict(data.prompt)
        return ModelResponseModel(
            output=response["output"],
        )
