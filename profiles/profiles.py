# -*- coding: utf-8 -*-

import sys
import yaml
import codecs
import re
from os import path
from jinja2 import Environment, PackageLoader

PROJECTS_PATH = path.join(path.dirname(__file__), 'projects')
OUTPUT_PATH = path.join(path.dirname(__file__), 'output')
env = Environment(loader=PackageLoader(__name__, 'templates'))


def usage():
    print 'Usage: profiles.py <recipe>'


def youtube_filter(text):
    return re.sub('\[(.*)\]\((.*)\)', '\\1: \\2', text)


def read_file(file_path):
    with codecs.open(file_path, "r", "utf-8") as f:
        return f.read()


def write_file(file_path, text):
    with codecs.open(file_path, "w+", "utf-8") as f:
        f.write(text)


def get_project_params(project_name):
    project_file_name = project_name + ".yaml"
    project_file_path = path.join(PROJECTS_PATH, project_file_name)
    return yaml.load(read_file(project_file_path))


def apply_filter(text, filter_name):
    if filter_name == 'Youtube':
        return youtube_filter(text)

    return text


def render_profile(project_name, template_name, filter_name):
    profile_file_name = "%s-%s-%s.md" % (project_name,
                                         template_name,
                                         filter_name)
    profile_file_path = path.join(OUTPUT_PATH, profile_file_name)
    project_params = get_project_params(project_name)
    template = env.get_template('%s.jinja2' % (template_name))

    print "Rendering %s" % (profile_file_path)

    write_file(profile_file_path,
               apply_filter(template.render(project_params), filter_name))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        exit(1)

    recipe = yaml.load(read_file(sys.argv[1]))

    for filter_name in [None] + recipe['filters']:
        for project_name in recipe['projects']:
            for template_name in recipe['templates']:
                render_profile(project_name,
                               template_name,
                               filter_name)
