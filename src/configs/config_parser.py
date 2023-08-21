"""
This module contains class to parse config(.ini) files and also its custom exception wrapper class.
"""
import configparser

class ConfigParserError(Exception):
    """This class acts as a wrapper class for catching exceptions."""


# Disabled too-few-public-methods since this class has a limited functionality.
class ConfigParser:  # pylint: disable=too-few-public-methods
    """This class parses config(.ini) files."""
    def __init__(self, _file):
        self.parse_config = configparser.ConfigParser()
        self.parse_config._interpolation = configparser.ExtendedInterpolation()
        self.parse_config.optionxform = str
        self.filename = _file
        filepath = f"./src/configs/{_file}"
        self.filepath = filepath if _file.endswith(".ini") else f"{filepath}.ini"
        parse_response = self.parse_config.read(self.filepath)

        if not parse_response:
            error = f"{self.filename} is not present in src/config."
            raise ConfigParserError(error)

    def get_configs(self, _key):
        """
        This function returns a dict of configs based on the _key.
        args:
            _key: str
        return: dict
        """
        if _key not in self.parse_config.sections():
            error = f"{_key} is not present in {self.filename}."
            raise ConfigParserError(error)

        return dict(self.parse_config[_key])
