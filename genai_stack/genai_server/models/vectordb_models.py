from pydantic import BaseModel


class DocumentType(BaseModel):
    page_content: str
    metadata: dict
