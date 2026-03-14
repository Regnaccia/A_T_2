import yaml

from app.validators.file_validator import file_exists, file_is_yaml

def file_loader(path):
    file_exists(path)
    file_is_yaml(path)
    config = load_config(path)
    return config

def load_config(path):
    import yaml
    with open(path, 'r') as file:
        try:
            config = yaml.safe_load(file)
            return config
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file: {e}")
