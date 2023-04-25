"""This module initializes logging object used for application level logging."""
import ast
import logging
import os
from datetime import datetime

from src.configs.config_parser import ConfigParser


class Logger:
    """This class initializes logging object used for application level logging."""

    def __init__(self, identifier):
        logs_directory = f"logs/{identifier}"
        os.makedirs(logs_directory, exist_ok=True)
        log_file = f"{logs_directory}/{datetime.now().strftime('%Y_%m_%d.log')}"
        logger_obj = logging.getLogger(identifier)

        for handler in logger_obj.handlers[:]:
            if isinstance(handler, logging.FileHandler):
                logger_obj.removeHandler(handler)

        file_handler = logging.FileHandler(log_file)
        config_parser = ConfigParser("config")
        configs = config_parser.get_configs("app_configs")
        formatter = logging.Formatter(configs["log_message_format"], configs["log_time_format"])
        file_handler.setFormatter(formatter)
        logger_obj.setLevel(logging.DEBUG)
        logger_obj.addHandler(file_handler)
        critical_log_libs = ast.literal_eval(configs["critical_log_libs"])
        for lib in critical_log_libs:
            # Log only critical logs for these libraries.
            logging.getLogger(lib).setLevel(logging.CRITICAL)
