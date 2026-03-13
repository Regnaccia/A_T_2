from pydantic import BaseModel, Field
from typing import Optional

class RouterConfig(BaseModel):
    sensors: Optional[list] = []