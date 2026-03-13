import yaml

def file_exists(path):
    if path.exists():
        return True
    else:
        raise FileNotFoundError(f"Configuration file not found at: {path}")
    
def file_is_yaml(path):
    if path.suffix in ['.yaml']:
        return True
    else:
        raise ValueError(f"Configuration file must be a YAML file: {path}")

