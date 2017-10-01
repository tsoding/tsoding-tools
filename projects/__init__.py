import yaml
from os import path
from easyfile import read_file


def get_project_params(project_name):
    return yaml.load(
        read_file(
            path.join(
                path.dirname(__file__),
                project_name + ".yaml"
            )
        )
    )
