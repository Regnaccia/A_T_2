from pathlib import Path
from app.loaders.yaml_loader import file_loader

from app.utils.loggher import log, indent_level
from app.utils.url import resolve_path

# loading system configuration
def load_instance_sensors(base_path, file_path, log_mode):
    path = resolve_path(base_path,file_path)

    file_name = str(path).split("\\")[-1]
    file_raw = file_loader(path)

    text = indent_level(f"✅ {file_name} loaded successfully",4)
    log(log_mode, text, print_if="verbouse")

    return file_raw