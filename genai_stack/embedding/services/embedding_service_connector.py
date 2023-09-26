import ast
from typing import Dict, List, Union
from pydantic import BaseModel
from requests import Session
from urllib.parse import urljoin

from genai_stack.services.service_connector import BaseServiceConnector

from .constants import EMBED_QUERY_ENDPOINT, EmbedQueryPayload


class ConnectionConfig(BaseModel):
    host: str
    port: int


class EmbeddingServiceConnector(BaseServiceConnector):
    def _post_init(self):
        super()._post_init()
        self.connection_config = ConnectionConfig(**self.service_config.get("connection_config"))
        self.embedding = self
        self.client = Session()

    def get_base_url(self):
        return f"http://{self.connection_config.host}:{self.connection_config.port}"

    def embed_query(self, text: Union[str, List[str]]):
        url = urljoin(self.get_base_url(), EMBED_QUERY_ENDPOINT)
        response = self.client.post(url, json=EmbedQueryPayload(query=text).dict())
        if not response.ok:
            raise ValueError(f"{response.content}")
        return self.postprocess(response_content=response.content)

    def embed_documents(self, texts: List[str]):
        return self.embed_query(texts)

    def postprocess(self, response_content: bytes):
        # Convert the byte string to a regular string
        string = response_content.decode("utf-8")

        # Remove enclosing single quotes and evaluate the string to obtain a list of floats
        lst = ast.literal_eval(string)

        # Ensure that the elements in the list are floats
        list_floats = [float(x) for x in lst]
        return list_floats
