from typing import Any
from llaim.model.base import BaseModel
from langchain.llms import OpenAIChat


class OpenAIGpt35Model(BaseModel):
    model_name = "Gpt 3.5"
    compulsory_fields = ["openai_api_key"]

    def load(self, model_path: str):
        return super().load(model_path)

    def predict(self, query: str):
        retriever_results = self.retriever.retrieve(query)
        query = query.decode("utf-8")

        # set api key as environment variables.
        # os.environ["OPENAI_API_KEY"] = "sk-xxxx"
        response = OpenAIChat(openai_api_key=self.model_config_fields.get("openai_api_key"), model="gpt-3.5-turbo")
        return response.choices[0].message.content
