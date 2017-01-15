# -*- coding: utf-8 -*-

import codecs


def read_file(file_path):
    with codecs.open(file_path, "r", "utf-8") as f:
        return f.read()


def write_file(file_path, text):
    with codecs.open(file_path, "w+", "utf-8") as f:
        f.write(text)
