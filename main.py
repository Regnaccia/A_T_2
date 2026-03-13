from pathlib import Path
from app.loaders.system_loader import load_system

# log_mode = "debug"
log_mode = "verbouse"
# log_mode = None

# Define paths
base_path = Path(__file__).parent

load_system(log_mode, base_path)