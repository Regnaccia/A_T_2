from app.utils.loggher import log, indent_level

from app.loaders.system_config_loader import load_system_config
from app.loaders.instance_config_loader import load_instance_config

from app.validators.system_config_validator import validate_system_config
from app.validators.instance_config_validator import validate_instance_config

from app.assembler.system_assembler import SystemAssembler
from app.assembler.instance_assembler import InstanceAssembler

class ConfigurationAssebbler:
    def __init__(self, log_mode, base_path, system_file):
        self.base_path = base_path
        self.system_file = system_file
        self.log_mode = log_mode

        self.system_config = None
        self.instances = None
        
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

            
        