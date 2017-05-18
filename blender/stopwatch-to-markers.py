import bpy
import csv
from os import path

scene = bpy.context.scene
blender_filepath = bpy.data.filepath
stopwatch_filename = "1495032354sec"
stopwatch_filepath = path.join(path.dirname(blender_filepath),
                               stopwatch_filename)
fps = 30


def read_csv(csv_file_name):
    with open(csv_file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        return [(name, int(seconds)) for (name, seconds) in csvreader]


def seconds_to_frame(seconds):
    return seconds * fps


for (name, seconds) in read_csv(stopwatch_filepath):
    scene.timeline_markers.new(name, seconds_to_frame(seconds))
