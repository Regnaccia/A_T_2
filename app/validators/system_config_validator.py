from pydantic import BaseModel
from typing import Optional

from app.types.SystemConfig import SystemConfig
from app.types.PackageConfig import PackageConfig
from app.types.MqttConfig import MqttConfig

def validate_system_config(file):
    validated = SystemConfig(**file)
    return validated

def validate_mqtt_config(file):
    validated = MqttConfig(**file)
    return validated


def validate_package_config(file):
    def test_exist(entities, type:str):
        istances = len([x for x in entities if x.type == type and x.initialize == True])
        if istances == 0:
            raise ValueError(f"❌ no {type} istances found")
        
    def test_single(entities, type:str):
        istances = len([x for x in entities if x.type == type and x.initialize == True])
        if istances > 1:
            raise ValueError("❌ more than 1 system istances found")

    validated = [PackageConfig(**x) for x in file]
    test_exist(validated,"system")
    test_single(validated,"system")

    test_exist(validated,"common")
    test_single(validated,"common")
    

    return validated
