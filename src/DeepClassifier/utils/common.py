import os
from box.exceptions import BoxValueError
import yaml
from DeepClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml_file(filepath: Path) -> ConfigBox:
    """
    This function is responsible for reading the content of YAML file,
    for which the path is passed, and returns the content of the file.
    Parameters
    ----------
    path_to_yaml : str
        File path for the YAML file.

    Raises
    ------
    ValueError:
        if yaml file is empty
    e:
        empty file

    Returns
    -------
    ConfigBox : ConfigBox type
        Content of the YAML file .
    """
    try:
        with open(filepath, "r") as file_obj:
            file_content = yaml.safe_load(file_obj)
            logger.info(f"Loaded the content from {filepath} successfully")
        return ConfigBox(file_content)
    except BoxValueError:
        raise ValueError("YAML file is empty.")
    except Exception as e:
        raise e


@ensure_annotations
def make_directories(paths: list, verbose: bool = True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    try:
        for path in paths:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"{path} created successfully.")
    except Exception as e:
        raise e


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_file_size(filepath: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(filepath) / 1024)
    return f"~ {size_in_kb} KB"
