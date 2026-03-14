from app.types.MqttConfig import MqttConfig

from app.utils.loggher import log, indent_level

def validate_mqtt_config(file,log_mode):
    validated = MqttConfig(**file)
    text = indent_level("✅ MQTT configuration validated successfully", 2)
    log(log_mode, text, print_if="verbouse")
    return validated