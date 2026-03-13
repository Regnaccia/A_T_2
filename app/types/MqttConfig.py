from pydantic import BaseModel, Field
from typing import Optional

class MqttConfig(BaseModel):
    broker: str = Field(min_length=1, strip_whitespace=True)
    port: str = Field(min_length=1, strip_whitespace=True)
    username: str = Field(min_length=1, strip_whitespace=True)
    password: str = Field(min_length=1, strip_whitespace=True)

