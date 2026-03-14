from app.utils.loggher import log, indent_level

from app.assembler.system_assembler import SystemAssembler
from app.assembler.instance_assembler import InstanceAssembler
from app.assembler.mqtt_assembler import MqttAssembler


class ConfigurationAssebbler:
    def __init__(self, log_mode, base_path, system_file):
        self.base_path = base_path
        self.system_file = system_file
        self.log_mode = log_mode

        self.system_config = None
        self.instances = None
        self.configuration = None
        
    def assemble(self):
        self._print_sequence("Assembling System")

        self._print_sequence("Loading Configuration")
        self.system_config = self._assemble_system()

        self._print_sequence("Loading Instances")
        self.instances = self._assemble_istances()

    def _assemble_system(self):
        system_assembler = SystemAssembler(
            base_path= self.base_path,
            file_path= self.system_file,
            log_mode= self.log_mode
        )
        system_assembler.assemble()
        return system_assembler
    
    def _assemble_istances(self):
        instances = []
        for instance in self.system_config.instance_manifest:
            instances_assembler = InstanceAssembler(
                base_path= self.base_path,
                instance= instance,
                log_mode= self.log_mode
            )
            instances_assembler.assemble()
            instances.append(instances_assembler)
        return instances
    
    def build(self):

        system = self._build_system()
        mqtt = self._build_mqtt()
        instances = self._build_instances()
        entities = self._build_entities()

        isntances = self._add_entities_to_instances(instances, entities)

        compiled = {
            "system": system,
            "mqtt": mqtt,
            "instances": instances,
            "entities": entities
        }
        self.built_config = compiled
    
    def _build_system(self):
        instances = [i.id for i in self.system_config.instance_manifest]
        system_info = {
            "name": self.system_config.name,
            "instances" : instances,
            "instances_count" : len(instances)
        }
        return system_info
    
    def _build_instances(self):
        instances_info = []
        for i in self.instances:
            instance_info = {
                "id": i.id,
                "name": i.name,
                "type": i.type,
                "info": {
                    "router": i.router_path 
                }
            }
            instances_info.append(instance_info)
        return instances_info

    def _build_entities(self):
        sensors_list_raw = []
        for i in self.instances:
            sensors = i.sensors
            for key, sensor in sensors: 
                sensors_list_raw = sensors_list_raw + sensor

        sensors_list =[]
        for sensor in sensors_list_raw:
            s = sensor.model_dump()
            s['full_id'] = s["parent"] + "_" + s['id']
            sensors_list.append(s)
        return sensors_list

    def _add_entities_to_instances(self, instances, entities):
        for i in instances:
            i['info']['sensors'] = [e["id"] for e in entities if e["parent"] == i["id"]]
            i['info']['sensors_count'] = len(i['info']['sensors'])
        return instances

    def _build_mqtt(self):
        mqtt = self.system_config.mqtt_config.model_dump()
        return mqtt

    def _print_sequence(self, stage):
        match stage:
            case "Assembling System":
                text = indent_level("⚙️ Assembling System",0)
                log(self.log_mode, text, print_if="verbouse")

            case "Loading Configuration":
                text = indent_level("⏳ Loading Configuration",1)
                log(self.log_mode, text, print_if="verbouse")

            case "Loading Instances":
                text = indent_level("⏳ Loading Instances",1)
                log(self.log_mode, text, print_if="verbouse")

    def print_config(self):
        self.system_config.print_config()
        print ("----------")
        for i in self.instances:
            i.print_config()

            
        