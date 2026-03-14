from pathlib import Path
from app.assembler.configuration_assembler import ConfigurationAssebbler
from app.builder.configuration_builder import configuration_builder

# log_mode = "debug"
log_mode = "verbouse"
# log_mode = None

# Define paths
base_path = Path(__file__).parent
system_file = "config\\00_system\\00_system.yaml"

configuration = ConfigurationAssebbler(
    log_mode = log_mode,
    base_path = base_path,
    system_file = system_file
    )

configuration.assemble()
configuration.build()
print(configuration.built_config)
# configuration.print_config()

