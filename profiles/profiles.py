# -*- coding: utf-8 -*-

import sys
import yaml
import re
from easyfile import read_file, write_file
from os import path
from jinja2 import Environment, PackageLoader

PROJECTS_PATH = path.join(path.dirname(__file__), 'projects')
OUTPUT_PATH = path.join(path.dirname(__file__), 'output')
env = Environment(loader=PackageLoader(__name__, 'templates'))


def usage():
    print 'Usage: profiles.py <recipe>'


def unmarkdown_links(text):
    return re.sub('\[(.*)\]\((.*)\)', '\\1: \\2', text)


def get_project_params(project_name):
    project_file_name = project_name + ".yaml"
    project_file_path = path.join(PROJECTS_PATH, project_file_name)
    return yaml.load(read_file(project_file_path))


def apply_filter(text, filter_name):
    if filter_name == 'Youtube':
        return unmarkdown_links(text)

    return text


def profile_file_name(project_name, template_name, filter_name):
    return "%s-%s-%s.md" % (project_name, template_name, filter_name)


def profile_file_path(project_name, template_name, filter_name):
    return path.join(OUTPUT_PATH,
                     profile_file_name(project_name,
                                       template_name,
                                       filter_name))


def render_profile(project_name, template_name, filter_name):
    project_params = get_project_params(project_name)
    template = env.get_template('%s.jinja2' % (template_name))

    return apply_filter(template.render(project_params), filter_name)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        exit(1)

    recipe = yaml.load(read_file(sys.argv[1]))

    for filter_name in [None] + recipe['filters']:
        for project_name in recipe['projects']:
            for template_name in recipe['templates']:
                output_file_path = profile_file_path(project_name,
                                                     template_name,
                                                     filter_name)

                print "Rendering %s" % (output_file_path)

                write_file(output_file_path,
                           render_profile(project_name,
                                          template_name,
                                          filter_name))
