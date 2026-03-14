from app.utils.loggher import log, indent_level

from app.loaders.mqtt_config_loader import load_mqtt_config

from app.validators.system_config_validator import validate_system_config


class MqttAssembler:
    def __init__(self, log_mode, base_path, file_path):
        self.base_path = base_path
        self.system_file = file_path
        self.log_mode = log_mode

        self.name = None
        self.instances_package = None
        
    def assemble(self):
        valid_model = self._load_and_validate_system_config()
        self.name = valid_model.system_name
        self.instances_package = valid_model.instances_package


    def _load_and_validate_mqtt_config(self):
        raw = load_mqtt_config(
            base_path= self.base_path,
            file_path= self.system_file,
            log_mode= self.log_mode  
            )
        
        validated = validate_system_config(raw, log_mode=self.log_mode)
        return validated    
    
    def print_config(self):
        print(13*"- " + " SYSTEM MQTT " + 13*"- ")
        for e in self.__dict__:
            print(f"{e} :    {self.__getattribute__(e)}")

            
        