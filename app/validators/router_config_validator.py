from app.types.RouterConfig import RouterConfig
from app.utils.loggher import log, indent_level

def validate_router_config(file, log_mode):
    validated = RouterConfig(**file)
    text = indent_level("✅ Instances router validated successfully", 3)
    log(log_mode, text, print_if="verbouse")
    return validated