from easyfile import read_yaml_file
from os.path import expanduser


# TODO(#18): configuration scheme
#
# Maintain actual configuration scheme and verify it on any
# configuration loading
def home_tsoding_config():
    return read_yaml_file(expanduser("~/.tsoding.yaml"))
