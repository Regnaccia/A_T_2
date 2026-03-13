from pathlib import Path
import yaml
from app.loaders.yaml_file_loader import file_loader
from app.loaders.sensors_loader import sensor_loader

from app.validators.system_config_validator import validate_system_config
from app.validators.system_config_validator import validate_mqtt_config
from app.validators.system_config_validator import validate_package_config
from app.validators.router_config_validator import validate_router_config

from app.log.loggher import log

def load_system(log_mode, base_path):
    text = "⏳ Loading System"
    log(log_mode, text, print_if="verbouse")

    # ---------------------------------------------------------------

    text = "     ⏳ Loading Configuration"
    log(log_mode, text, print_if="verbouse")

    # ---------------------------------------------------------------

    # loading system configuration
    system_config_path = Path("/01_config/00_system/00_system.yaml")
    path = Path(str(base_path) + str(system_config_path))

    system_config_raw = file_loader(path)
    text = "     ✅ System configuration loaded successfully:"
    log(log_mode, text, print_if="verbouse")

    # validating system configuration
    system_config = validate_system_config(system_config_raw)
    text = "     ✅ System configuration validated successfully:"
    log(log_mode, text, print_if="verbouse")

    for key, el in system_config:
        text = key + ": " + str(el)
        log(log_mode, text, print_if="debug")

    # ---------------------------------------------------------------

    # loading instances package
    instances_package_path = system_config.instances_package
    path = Path(str(base_path) + str(instances_package_path))

    instances_package_raw = file_loader(path)
    text = "     ✅ Instances package loaded successfully:"
    log(log_mode, text, print_if="verbouse")

    # validating instances package
    instances_package = validate_package_config(instances_package_raw)
    text = "     ✅ Instances package validated successfully:"
    log(log_mode, text, print_if="verbouse")

    # ---------------------------------------------------------------
    # loading instances routers
    for i in instances_package:
        instance_router_path = i.router
        path = Path(str(base_path) + str(instance_router_path))
        instance_router_raw = file_loader(path)
        text = f"       ✅ {i.name} router loaded successfully:"
        log(log_mode, text, print_if="verbouse")

        instance_router = validate_router_config(instance_router_raw)
        text = f"       ✅ {i.name} router validated successfully:"
        log(log_mode, text, print_if="verbouse")

        # adding dependecy from router
        router_element = instance_router.model_dump()
        for key in router_element.keys():
            text = f"           ⏳ loading {i.name} {key}"
            log(log_mode, text, print_if="verbouse")
            lst = router_element[key]
            files_raw = []
            for file_path in lst:
                path = Path(str(base_path) + str(file_path))
                file_raw = file_loader(path)
                file_name = str(file_path).split("\\")[-1]
                if file_raw is not None:
                    files_raw.append(file_raw)
                    text = f"               ✅ {file_name} loaded successfully:"
                    log(log_mode, text, print_if="verbouse")

            if key == "sensors":
                sensors = sensor_loader(files_raw)
                    
                
            

    for i in instances_package:
        for key, el in i:
            text = key + ": " + str(el)
            log(log_mode, text, print_if="debug")
        text = "------------"
        log(log_mode, text, print_if="debug")

    # ---------------------------------------------------------------

    # loading mqtt configuration
    mqtt_config_path = system_config.mqtt_config
    path = Path(str(base_path) + str(mqtt_config_path))

    mqtt_config_raw = file_loader(path)
    text = "     ✅ MQTT configuration loaded successfully:"
    log(log_mode, text, print_if="verbouse")

    # validating mqtt configuration
    mqtt_config = validate_mqtt_config(mqtt_config_raw)
    text = "     ✅ MQTT configuration validated successfully:"
    log(log_mode, text, print_if="verbouse")

    for key, el in mqtt_config:
        text = key + ": " + str(el)
        log(log_mode, text, print_if="debug")


if __name__ == "__main__":
    log_mode = "debug"
    # log_mode = "verbouse"
    # log_mode = None
    base_path = base_path = Path(__file__).parent.parent
    load_system(log_mode, base_path)







