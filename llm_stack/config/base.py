from pydantic import BaseModel


class BaseFieldConfig(BaseModel):
    pass


class BaseComponentConfig(BaseModel):
    name: str
    fields: BaseFieldConfig
