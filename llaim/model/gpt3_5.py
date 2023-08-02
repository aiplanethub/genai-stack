from typing import Any
from langchain.llms import OpenAIChat
import json
from langchain.schema import Generation

from llaim.model.base import BaseModel
from .prompts import BASIC_QA


class OpenAIGpt35Model(BaseModel):
    model_name = "Gpt_3.5"
    compulsory_fields = ["openai_api_key"]

    def load(self, model_path: str):
        return super().load(model_path)

    def predict(self, query: str):
        query = query.decode("utf-8")
        print(query)
        retriever_results = self.retriever.retrieve(query)

        prompt = BASIC_QA.format(context=retriever_results, user_prompt=query)
        openai_chat = OpenAIChat(openai_api_key=self.model_config_fields.get("openai_api_key"), model="gpt-3.5-turbo")
        response = openai_chat.generate(prompts=[prompt])
        response = {
            "response": "".join(self.parse_generations(response.generations)),
            "metadata": response.llm_output,
        }
        return json.dumps(response)

    def parse_generations(self, generation_lst: list):
        """
        Recursively parse the text in the generations
        """
        result = """"""

        for g in generation_lst:
            if isinstance(g, list):
                result += self.parse_generations(g)
            if isinstance(g, Generation):
                result += g.text

        return result
