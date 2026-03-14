from app.utils.loggher import log, indent_level

from app.loaders.instance_router_loader import load_instance_router
from app.loaders.instance_sensors_loader import load_instance_sensors

from app.validators.router_config_validator import validate_router_config
from app.validators.instance_sensors_manifest_validator import validate_instance_sensor_model


class InstanceAssembler:
    def __init__(self,log_mode, base_path, instance):
        self.base_path = base_path
        self.log_mode = log_mode

        self.id = instance.id
        self.name = instance.name
        self.type = instance.type
        self.router_path = instance.router

        self.router = None

    def assemble(self):
        text = indent_level(f"⚙️ Assembling Instance {self.name}",2)
        log(self.log_mode,text,"verbouse")
        valid_model = self._load_and_validate_router()
        self.router = valid_model

        text = indent_level(f"⚙️ Assembling Instance Sensors",3)
        log(self.log_mode,text,"verbouse")
        sensors = self._load_and_validate_sensors()
        sensors = self._aggragate_sensors_by_type(sensors)
        self.sensors = self._validate_sensors(sensors)
        
    def _load_and_validate_router(self):
        raw = load_instance_router(
            base_path= self.base_path,
            file_path= self.router_path,
            log_mode= self.log_mode
            )
        validated = validate_router_config(raw, self.log_mode)
        return validated
    
    def _load_and_validate_sensors(self):
        sensors_files = self.router.sensors
        sensors = []
        for sensor_file in sensors_files:
            raw = load_instance_sensors(
                base_path= self.base_path,
                file_path= sensor_file,
                log_mode= self.log_mode
            )
            sensors.append(raw)
        return sensors

    def _aggragate_sensors_by_type(self, sensors):
        aggregated = {}
        for x in sensors:
            if x != None:
                for key , value in x.items():
                    if key not in aggregated.keys():
                        aggregated[key] = []
                    
                    for s in value:
                        aggregated[key].append(s)

        return aggregated

    def _validate_sensors(self,sensors):
        validated = validate_instance_sensor_model(sensors, self.log_mode)
        return validated
        
        
        


    def print_config(self):
        print(13*"- " + f" INSTANCE {self.name} CONFIG " + 13*"- ")
        for e in self.__dict__:
            print(f"{e} :    {self.__getattribute__(e)}")

            
        