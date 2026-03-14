from pydantic import BaseModel, Field, model_validator
from typing import Optional, Literal
from collections import Counter

class BaseSensor(BaseModel):
    id: str
    name: str
    type: Literal["internal", "input", "output"]

class Sensor(BaseSensor):
    pass

class BinarySensor(BaseSensor):
    pass

class InstanceSensorManifest(BaseModel):
    sensor: list[Sensor] = Field(default_factory=list)
    binary_sensor: list[BinarySensor] = Field(default_factory=list)

    @model_validator(mode="after")
    def normalize_entities(self):
        all_ids = [x.id for x in self.sensor] + [x.id for x in self.binary_sensor]
        counts = Counter(all_ids)
        duplicates = [k for k, v in counts.items() if v > 1]
        if duplicates:
            raise ValueError(f"Duplicate entity ids: {duplicates}")

        return self


