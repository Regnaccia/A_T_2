from pathlib import Path
from app.loaders.yaml_loader import file_loader

from app.utils.loggher import log, indent_level
from app.utils.url import resolve_path

# loading system configuration
def load_mqtt_config(base_path, file_path, log_mode):
    
    path = resolve_path(base_path,file_path)

    system_config_raw = file_loader(path)

    text = indent_level("✅ MQTT configuration loaded successfully",2)
    log(log_mode, text, print_if="verbouse")

    return system_config_raw