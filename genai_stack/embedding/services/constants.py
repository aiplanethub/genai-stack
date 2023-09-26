from pydantic import BaseModel
from typing import List, Union

EMBED_QUERY_ENDPOINT = "/embed-query"


class EmbedQueryPayload(BaseModel):
    query: Union[str, List[str]]
