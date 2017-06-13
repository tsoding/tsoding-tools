# -*- coding: utf-8 -*-

import codecs
import yaml
import csv
import json

from functools import partial


def read_file(file_path):
    """Just read the whole content from file"""
    with codecs.open(file_path, "r", "utf-8") as f:
        return f.read()


def write_file(file_path, text):
    """Just write text to file"""
    with codecs.open(file_path, "w+", "utf-8") as f:
        f.write(text)


def with_write_file(file_path, action):
    with codecs.open(file_path, "w+", "utf-8") as f:
        action(f)


def read_yaml_file(file_path):
    """Read and parse YAML file"""
    return yaml.load(read_file(file_path))


def write_json_file(file_path, data):
    with_write_file(file_path, partial(json.dump, data))


def write_csv_file(file_path, table):
    if len(table) <= 0:
        return

    fieldnames = table[0].keys()

    with codecs.open(file_path, "w+", "utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in table:
            writer.writerow(row)
