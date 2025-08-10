import yaml
from pathlib import Path

def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(Path(config_path), "r") as file:
        config=yaml.safe_load(file)
    return config
