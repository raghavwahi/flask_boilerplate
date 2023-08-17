"""This module validates if all imported modules in 'src' are installed in the env."""
import logging
import os
from glob import glob

from src.utils.logger_util import Logger


def check_required_modules():
    """
    This function scans through directories to ensure that required modules are present.
    If an imported module is not installed, it triggers an error.
    """
    source = "src"
    default_logs = "generic"
    Logger(default_logs)
    logger = logging.getLogger(default_logs)
    source_path = os.path.join(os.getcwd(), source)
    folders = os.listdir(source_path)

    for folder in folders:
        if folder.startswith("__"):
            continue
        folder_dir = os.path.join(source_path, folder)
        package_name = f"{source}.{folder}."
        logger.info("Importing dir: %s", package_name)

        for file in glob(os.path.join(folder_dir, "*.py")):
            if not file.startswith("__"):
                __import__(f"{package_name}{os.path.basename(file)[:-3]}", globals(), locals())
