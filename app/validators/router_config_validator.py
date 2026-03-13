from app.types.RouterConfig import RouterConfig

def validate_router_config(file):
    validated = RouterConfig(**file)
    return validated