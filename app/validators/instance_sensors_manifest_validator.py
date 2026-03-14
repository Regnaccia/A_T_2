from app.types.InstanceSensors import InstanceSensorManifest

from app.utils.loggher import log, indent_level

def validate_instance_sensor_model(file, log_mode):
    validated = InstanceSensorManifest(**file)
    text = indent_level("✅ validated successfully", 4)
    log(log_mode, text, print_if="verbouse")
    return validated
