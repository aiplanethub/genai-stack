from typing import Any
import openai
from llaim.model.base import BaseModel


class OpenAIGpt35Model(BaseModel):
    name = "Gpt 3.5"

    def load(self, model_path: str):
        return super().load(model_path)

    def predict(self, query: Any):
        query = query.decode("utf-8")

        # set api key as environment variables.
        # os.environ["OPENAI_API_KEY"] = "sk-xxxx"
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query},
            ],
            temperature=0.7,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return res.choices[0].message.content
