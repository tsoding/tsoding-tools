import sys
import yaml
from os import path
from jinja2 import Environment, PackageLoader

PROJECTS_PATH = path.join(path.dirname(__file__), 'projects')
env = Environment(loader=PackageLoader(__name__, 'templates'))


def usage():
    print 'Usage: profiles.py <project> <template>'


def get_project_params(project_name):
    project_file_name = project_name + ".yaml"
    project_file_path = path.join(PROJECTS_PATH, project_file_name)
    with open(project_file_path, "r") as project_file:
        return yaml.load(project_file.read())


if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        exit(1)

    project_name = sys.argv[1]
    template_name = sys.argv[2]

    project_params = get_project_params(project_name)
    template = env.get_template('%s.jinja2' % (template_name))

    print template.render(project_params)
