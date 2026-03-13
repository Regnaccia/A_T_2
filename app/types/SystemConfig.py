from pydantic import BaseModel, Field
from typing import Optional

class SystemConfig(BaseModel):
    system_name: str = Field(min_length=1, strip_whitespace=True)
    mqtt_config: str = Field(min_length=1, strip_whitespace=True)
    instances_package: str = Field(min_length=1, strip_whitespace=True)


