from app.types.SystemConfig import SystemConfig
from app.types.MqttConfig import MqttConfig

from app.utils.loggher import log, indent_level

def validate_system_config(file, log_mode):
    validated = SystemConfig(**file)
    text = indent_level("✅ System configuration validated successfully", 2)
    log(log_mode, text, print_if="verbouse")
    return validated

def validate_mqtt_config(file):
    validated = MqttConfig(**file)
    return validated



