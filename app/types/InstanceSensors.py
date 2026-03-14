from pydantic import BaseModel, Field, model_validator
from typing import Optional, Literal
from collections import Counter

class BaseSensor(BaseModel):
    id: str
    name: str
    type: Literal["internal", "input", "output"]
    parent: str

class Sensor(BaseSensor):
    domain: str = "sensor" 

class BinarySensor(BaseSensor):
    domain: str = "binary_sensor" 

class Select(BaseSensor):
    domain: str = "select" 

class InstanceSensorManifest(BaseModel):
    sensor: list[Sensor] = Field(default_factory=list)
    binary_sensor: list[BinarySensor] = Field(default_factory=list)
    select: list[Select] = Field(default_factory=list)

    @model_validator(mode="after")
    def normalize_entities(self):
        l = []
        l.append( [x.id for x in self.sensor] )
        l.append( [x.id for x in self.binary_sensor] )
        l.append( [x.id for x in self.select] )

        all_ids = []
        for e in l:
            all_ids = all_ids + e
        counts = Counter(all_ids)
        duplicates = [k for k, v in counts.items() if v > 1]
        if duplicates:
            raise ValueError(f"Duplicate entity ids: {duplicates}")

        return self


