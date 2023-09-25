import json
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import root_validator

from genai_stack.embedding.base import BaseEmbedding
from genai_stack.services.local import LocalService, LocalServiceConfig
from genai_stack.utils.network import find_available_port

from .constants import EMBED_QUERY_ENDPOINT, EmbedQueryPayload


class EmbeddingServiceConfig(LocalServiceConfig):
    embedding_component: BaseEmbedding

    class Config:
        arbitrary_types_allowed = True


class EmbeddingService(LocalService):
    config_class = EmbeddingServiceConfig

    def setup(self):
        super().setup()
        self.host = "127.0.0.1"
        self.port = find_available_port()

    def run(self):
        app = FastAPI()
        embedding = self.config.embedding_component

        @app.post(EMBED_QUERY_ENDPOINT)
        async def embed_query(request: Request):
            nonlocal embedding

            body = await request.json()
            parsed_body = EmbedQueryPayload(**body)

            embeddings = None
            if isinstance(parsed_body.query, str):
                embeddings = embedding.embed_text(text=parsed_body.query)
            elif isinstance(parsed_body.query, list):
                embeddings = embedding.embedding.embed_documents(texts=parsed_body.query)

            return JSONResponse(content=json.dumps(embeddings))

        uvicorn.run(app, host=self.host, port=self.port)

    def store_to_registry(self, exclude={"embedding_component", "config_output_path"}):
        return super().store_to_registry(exclude)

    def _get_service_metadata(self):
        return {"connection_config": {"host": self.host, "port": self.port}}
