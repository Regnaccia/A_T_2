from pathlib import Path
import yaml
from app.loaders.yaml_file_loader import file_loader

base_path = Path(__file__).parent

file_path = Path("\\01_config\\01_instances\\01_system_package.yaml")
path = Path(str(base_path) + str(file_path))

a = file_loader(path)
print(a)