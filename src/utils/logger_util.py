"""This module initializes logging object used for application level logging."""
import ast
import logging
import os
from datetime import datetime

from src.configs.config_parser import ConfigParser


# Disabled too-few-public-methods since this class has a limited functionality.
class Logger:  # pylint: disable=too-few-public-methods
    """This class initializes logging object used for application level logging."""

    def __init__(self, identifier):
        logs_directory = f"logs/{identifier}"
        os.makedirs(logs_directory, exist_ok=True)
        log_file = f"{logs_directory}/{datetime.now().strftime('%Y_%m_%d.log')}"
        logger_obj = logging.getLogger(identifier)
        stream_handler_added = False

        for handler in logger_obj.handlers:
            if isinstance(handler, logging.FileHandler):
                logger_obj.removeHandler(handler)
            if isinstance(handler, logging.StreamHandler):
                stream_handler_added = True

        config_parser = ConfigParser("config")
        configs = config_parser.get_configs("app_configs")
        file_formatter = logging.Formatter(configs["log_file_message_format"],
                                           configs["log_time_format"])
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(file_formatter)
        logger_obj.addHandler(file_handler)

        if not stream_handler_added:
            stream_formatter = logging.Formatter(
                configs["log_stream_message_format"].format(identifier=identifier),
                configs["log_time_format"],
            )
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(stream_formatter)
            logger_obj.addHandler(stream_handler)

        logger_obj.setLevel(logging.DEBUG)
        critical_log_libs = ast.literal_eval(configs["critical_log_libs"])
        for lib in critical_log_libs:
            # Log only critical logs for these libraries.
            logging.getLogger(lib).setLevel(logging.CRITICAL)
