import logging
import configparser
import os

class ConfigUtility:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(os.path.join(os.getcwd(),"config.ini"))
        logging.info('Init the config file')

    def ConfigSectionMap(self, section):
        config_dict = {}
        for option in self.config.options(section):
            config_dict[option] = self.config.get(section, option)
        return config_dict

ConfigUtility.__doc__ ="This class is used for reading and loading the configurations of UI elements " \
                       "and also includes the path of image directory where all the card images are stored"