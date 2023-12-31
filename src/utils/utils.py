
from pathlib import Path
from time import sleep
from winsound import Beep
import logging
import pickle
import yaml

logger = logging.getLogger(__name__)


def read_yaml(file_path: str):
    """
    Read data from a YAML file.

    Args:
        file_path (str): Path of the YAML file.

    Returns:
        object: Data loaded from the YAML file, or None if there is an error.
    """
    try:
        with open(Path(file_path)) as f:
            data = yaml.safe_load(f)
        logger.info("YAML file read: OK")
        return data
    except (FileNotFoundError, IOError, yaml.YAMLError) as err:
        logger.exception(f"Failed to read YAML file {file_path}: {err}")
        return None


def write_yaml(file_path: str, data: object):
    """
    Write data to a YAML file.

    Args:
        file_path (str): Path of the YAML file.
        data (object): Data to write.

    Returns:
        bool: True if the file was written successfully, False otherwise.
    """
    try:
        with open(Path(file_path), "w") as f:
            yaml.dump(data, f)
        logger.info("YAML file write: OK")
        return True
    except (FileNotFoundError, IOError, yaml.YAMLError) as err:
        logger.exception(f"Failed to write YAML file {file_path}: {err}")
        return False


def read_pickle(file_path: str):
    """
    Read data from a Pickle file.

    Args:
        file_path (str): Path of the Pickle file.

    Returns:
        object: Data loaded from the Pickle file, or None if there is an error.
    """
    try:
        with open(Path(file_path), "rb") as f:
            data = pickle.load(f)
        logger.info("Pickle file read: OK")
        return data
    except (FileNotFoundError, IOError, pickle.PickleError) as err:
        logger.exception(f"Failed to read Pickle file {file_path}: {err}")
        return None


def write_pickle(file_path: str, data: object):
    """
    Write data to a Pickle file.

    Args:
        file_path (str): Path of the Pickle file.
        data (object): Data to write.

    Returns:
        bool: True if the file was written successfully, False otherwise.
    """
    try:
        with open(Path(file_path), "wb") as f:
            pickle.dump(data, f)
        logger.info("Pickle file write: OK")
        return True
    except (FileNotFoundError, IOError, pickle.PickleError) as err:
        logger.exception(f"Failed to write Pickle file {file_path}: {err}")
        return False

def bee(r: int = 3, f: int = 2500, d: int = 1000, p: float = 1) -> None:
    """
    Emits a series of sounds using the Beep function from the winsound library.

    Args:
        r (int): Number of sound repetitions (default: 3).
        f (int): Sound frequency in Hz (default: 2500).
        d (int): Sound duration in milliseconds (default: 1000).
        p (float): Pause between each sound in seconds (default: 1).

    Returns:
        None
    """
    for n in range(r):
        Beep(f, d)
        sleep(p)

