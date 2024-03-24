import json
import os
from typing import Any, Dict

from .constants import SETTINGS_JSON_PATH
from .defaultsettings import DEFAULT_SETTINGS

JSON_INDENT = 4


class ApplicationSettings:
    """Class for storing SMD Converter configuration values
    """

    def __init__(self, settings_dict: Dict[str, Any], json_path: str) -> None:
        self.__settings_dict = settings_dict
        self.__json_path = json_path


class ApplicationSettingsHandler:
    """Class for managing json files that store configurations for discordbbcbot
    """

    def __init__(self, json_path: str = SETTINGS_JSON_PATH) -> None:
        self.__json_path = json_path

    def load(self) -> ApplicationSettings:
        if os.path.isfile(self.__json_path):  # check if settings file exists
            with open(self.__json_path, mode='r') as f:
                settings_dict = json.load(f)

        else:  # make settings file and load default settings
            print("Warning: Settings file does not exist.")
            self.save_default_settings()
            settings_dict = DEFAULT_SETTINGS

        return ApplicationSettings(settings_dict, self.__json_path)

    def save_default_settings(self) -> None:
        with open(self.__json_path, mode='w') as f:
            json.dump(DEFAULT_SETTINGS, f, indent=JSON_INDENT)
        print("Information: Default settings "
              f"were saved to {self.__json_path}.")
