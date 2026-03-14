from app.types.PackageConfig import PackageConfig

from app.utils.loggher import log, indent_level


def validate_instance_config(file, log_mode):
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

    text = indent_level("✅ Instances package validated successfully", 2)
    log(log_mode, text, print_if="verbouse")

    return validated