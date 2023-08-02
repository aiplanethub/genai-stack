from typing import Any
from langchain.llms import OpenAIChat

from llaim.model.base import BaseModel
from .prompts import BASIC_QA


class OpenAIGpt35Model(BaseModel):
    model_name = "Gpt_3.5"
    compulsory_fields = ["openai_api_key"]

    def load(self, model_path: str):
        return super().load(model_path)

    def predict(self, query: str):
        retriever_results = self.retriever.retrieve(query)
        query = query.decode("utf-8")

        prompt = BASIC_QA.format(context=retriever_results, user_prompt=query)
        # set api key as environment variables.
        # os.environ["OPENAI_API_KEY"] = "sk-xxxx"
        openai_chat = OpenAIChat(openai_api_key=self.model_config_fields.get("openai_api_key"), model="gpt-3.5-turbo")
        response = openai_chat.generate(prompts=[prompt])
        return response.llm_output
