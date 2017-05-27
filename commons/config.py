from easyfile import read_yaml_file
from os.path import expanduser


def home_tsoding_config():
    return read_yaml_file(expanduser("~/.tsoding.yaml"))
