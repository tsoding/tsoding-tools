# coding: utf-8

import sys
import csv
from jinja2 import Environment, PackageLoader


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def read_stopwatch(stopwatch_file):
    with open(stopwatch_file, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        return [[comment, int(secs)] for [comment, secs] in csvreader]


def stopwatch_to_parts(stopwatch):
    result = []
    count = 1
    for chunk in chunks(stopwatch, 2):
        if len(chunk) == 2:
            [[_, begin], [_, end]] = chunk
            result.append({
                'begin': begin,
                'length': end - begin + 1,
                'filename': 'part-%d.ts' % (count)
            })
            count += 1
    return result


def usage():
    print "Usage: makefile.py <morning-input> <stopwatch> <morning-output>"


if __name__ == '__main__':
    if len(sys.argv) < 4:
        usage()
        exit(1)

    morning_input = sys.argv[1]
    parts = stopwatch_to_parts(read_stopwatch(sys.argv[2]))
    morning_output = sys.argv[3]

    render_params = {
        "morning_input": morning_input,
        "morning_output": morning_output,
        "parts": parts,
        "parts_deps_list": " ".join([part["filename"] for part in parts]),
        "parts_concat_list": "|".join([part["filename"] for part in parts])
    }

    env = Environment(loader=PackageLoader(__name__, 'templates'))
    print env.get_template('Makefile.jinja2').render(render_params)
