from pydantic import BaseModel, Field   
from typing import Optional

class PackageConfig(BaseModel):
    id: str = Field(min_length=1, strip_whitespace=True)
    name: str = Field(min_length=1, strip_whitespace=True)
    type: str = Field(min_length=1, strip_whitespace=True)
    router: str = Field(min_length=1, strip_whitespace=True)
    initialize : Optional[bool] = True

