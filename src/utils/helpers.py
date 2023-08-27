"""This module contains helper methods used across the application."""
import ast

from src.configs.config_parser import ConfigParser


def fetch_request_methods():
    """
    This method fetches request methods from configuration file.
    return: dict
    """
    product_config = ConfigParser("config")
    configs = product_config.get_configs("app_configs")
    return ast.literal_eval(configs["request_methods"])
