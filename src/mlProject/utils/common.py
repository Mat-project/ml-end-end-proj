from box.exceptions import BoxValueError
import yaml
from mlProject.Logging import logger
import json
import joblib
import os
from box import ConfigBox
from pathlib import Path
from typing import Any


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns a ConfigBox object."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


def create_directories(path_to_directories: list, verbose=True):
    """Create a list of directories."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


def save_json(path: Path, data: dict):
    """Save JSON data."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


def load_json(path: Path) -> ConfigBox:
    """Load JSON file data."""
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


def save_bin(data: Any, path: Path):
    """Save binary file."""
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


def load_bin(path: Path) -> Any:
    """Load binary data."""
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


def get_size(path: Path) -> str:
    """Get size of file in KB."""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
