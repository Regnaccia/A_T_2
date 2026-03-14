from app.utils.loggher import log, indent_level



class InstanceAssembler:
    def __init__(self,log_mode, base_path, instance):
        self.base_path = base_path
        self.log_mode = log_mode

        self.id = instance.id
        self.name = instance.name
        self.type = instance.type
        self.router = instance.router


        
    def assemble(self):
        pass

    def print_config(self):
        print(13*"- " + f" INSTANCE {self.name} CONFIG " + 13*"- ")
        for e in self.__dict__:
            print(f"{e} :    {self.__getattribute__(e)}")

            
        