from easyfile import read_yaml_file
from os.path import expanduser


def get_tsoding_config():
    return read_yaml_file(expanduser("~/.tsoding.yaml"))
