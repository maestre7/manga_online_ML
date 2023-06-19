
from contextlib import contextmanager
from pathlib import Path
import logging
import yaml

logger = logging.getLogger(__name__)


@contextmanager
def handle_yaml_exceptions():
    try:
        yield
    except (FileNotFoundError, IOError, yaml.YAMLError):
        logger.exception('read_yaml')
        yield False
        

def read_yaml(file_path: str):
    """
    Read a YAML file and return the data in the saved format.

    Args:
        file_path (str): Path of the YAML file.

    Returns:
        TYPE DATA FILE: Data in the format saved in the YAML file.
        False: In case of an error.
    """

    with handle_yaml_exceptions():
        with open(Path(file_path), 'r') as file:
            data = yaml.safe_load(file)

    logger.info("YAML file read: OK")
    return data


def registro_yaml(destination: str, data, mode: str = "w"):
    """
    Writes the provided data to a YAML file.

    Args:
        destination (str): Path of the YAML file.
        data: Data to be written to the file.
        mode (str, optional): Writing mode. Defaults to "w".

    Returns:
        bool: True if the writing was successful, False if there was an error.
    """

    with handle_yaml_exceptions():
        with open(Path(destination), mode) as file:
            yaml.dump(data, file)

    logger.info("YAML file write: OK")
    return True

