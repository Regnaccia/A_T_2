from app.utils.loggher import log, indent_level

from app.loaders.instance_router_loader import load_instance_router
from app.validators.router_config_validator import validate_router_config


class InstanceAssembler:
    def __init__(self,log_mode, base_path, instance):
        self.base_path = base_path
        self.log_mode = log_mode

        self.id = instance.id
        self.name = instance.name
        self.type = instance.type
        self.router = instance.router

    def assemble(self):
        text = indent_level(f"⚙️ Assembling Instance {self.name}",2)
        log(self.log_mode,text,"verbouse")
        valid_model = self._load_and_validate_router()
        
    def _load_and_validate_router(self):
        raw = load_instance_router(
            base_path= self.base_path,
            file_path= self.router,
            log_mode= self.log_mode
            )
        
        validated = validate_router_config(raw, self.log_mode)
        return validated

    def print_config(self):
        print(13*"- " + f" INSTANCE {self.name} CONFIG " + 13*"- ")
        for e in self.__dict__:
            print(f"{e} :    {self.__getattribute__(e)}")

            
        