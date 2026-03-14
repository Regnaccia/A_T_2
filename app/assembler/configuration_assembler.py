from app.utils.loggher import log, indent_level


class Configuration:
    def __init__(self,log_mode, base_path, system_file):
        self.base_path = base_path
        self.system_file = system_file
        self.log_mode = log_mode 

        self.print_sequence("Assembling System")

        self.print_sequence("Loading Configuration")
        valid_model = self.load_and_validate_system_config()
        self.name = valid_model.system_name
        self.instances_package = valid_model.instances_package

        valid_model = self.load_and_validate_instance_config()
        self.instances = valid_model
        


    def load_and_validate_system_config(self):
        from app.loaders.system_config_loader import load_system_config
        from app.validators.system_config_validator import validate_system_config

        raw = load_system_config(
            base_path= self.base_path,
            file_path= self.system_file,
            log_mode= self.log_mode  
            )
        
        validated = validate_system_config(raw, log_mode=self.log_mode)

        return validated    
    
    def load_and_validate_instance_config(self):
        from app.loaders.instance_config_loader import load_instance_config
        from app.validators.instance_config_validator import validate_instance_config

        raw = load_instance_config(
            base_path= self.base_path,
            file_path= self.instances_package,
            log_mode= self.log_mode  
            )
        
        validated = validate_instance_config(raw, log_mode=self.log_mode)
        print(validated)
        return validated  
        
    def print_sequence(self, stage):
        match stage:
            case "Assembling System":
                text = indent_level("⚙️ Assembling System",0)
                log(self.log_mode, text, print_if="verbouse")

            case "Loading Configuration":
                text = indent_level("⏳ Loading Configuration",1)
                log(self.log_mode, text, print_if="verbouse")

    def print_config(self):
        print(13*"- " + " SYSTEM CONFIG " + 13*"- ")
        print(self.name)

            
        