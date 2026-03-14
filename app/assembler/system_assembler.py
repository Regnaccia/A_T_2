from app.utils.loggher import log, indent_level

from app.loaders.system_config_loader import load_system_config
from app.loaders.instance_config_loader import load_instance_config
from app.loaders.mqtt_config_loader import load_mqtt_config

from app.validators.system_config_validator import validate_system_config
from app.validators.instance_config_validator import validate_instance_config
from app.validators.mqtt_config_validator import validate_mqtt_config

class SystemAssembler:
    def __init__(self, log_mode, base_path, file_path):
        self.base_path = base_path
        self.system_file = file_path
        self.log_mode = log_mode

        self.name = None
        self.instances_package = None
        self.mqtt_config = None
        
    def assemble(self):
        valid_model = self._load_and_validate_system_config()
        self.name = valid_model.system_name

        self.instances_package = valid_model.instances_package
        self.mqtt_path = valid_model.mqtt_config
        
        valid_model = self._load_and_validate_instance_config()        
        self.instance_manifest = valid_model
        
        valid_model = self._load_and_validate_mqtt_config()   
        self.mqtt_config = valid_model     
        

    def _load_and_validate_system_config(self):
        raw = load_system_config(
            base_path= self.base_path,
            file_path= self.system_file,
            log_mode= self.log_mode  
            )
        
        validated = validate_system_config(raw, log_mode=self.log_mode)
        return validated    

    def _load_and_validate_instance_config(self):
        raw = load_instance_config(
            base_path= self.base_path,
            file_path= self.instances_package,
            log_mode= self.log_mode  
            )
        
        validated = validate_instance_config(raw, log_mode=self.log_mode)
        return validated  

    def _load_and_validate_mqtt_config(self):
        raw = load_mqtt_config(
            base_path= self.base_path,
            file_path= self.mqtt_path,
            log_mode= self.log_mode  
            )
        
        validated = validate_mqtt_config(raw, log_mode=self.log_mode)
        return validated  

    def print_config(self):
        print(13*"- " + " SYSTEM CONFIG " + 13*"- ")
        for e in self.__dict__:
            print(f"{e} :    {self.__getattribute__(e)}")

            
        