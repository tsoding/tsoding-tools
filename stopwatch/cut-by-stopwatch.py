import csv
import bpy

def read_csv(csv_file_name):
    with open(csv_file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        return [[comment, int(secs)] for [comment, secs] in csvreader]

def cut_at(frame):
    bpy.ops.sequencer.select_all(action='SELECT')
    bpy.ops.sequencer.cut(frame=frame, type='SOFT')

fps = bpy.data.scenes['Scene'].render.fps / bpy.data.scenes['Scene'].render.fps_base
stopwatch = "/home/rexim/MorningTsoding/Morganey/Ep.27/1480862482sec"

cut_at(0)
for [_, secs] in read_csv(stopwatch):
    cut_at(secs * fps)
