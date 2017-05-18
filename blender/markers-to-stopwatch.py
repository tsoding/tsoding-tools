import bpy
import csv
from os import path

scene = bpy.context.scene
blender_filepath = bpy.data.filepath
stopwatch_filename = "stopwatch.csv"
stopwatch_filepath = path.join(path.dirname(blender_filepath),
                               stopwatch_filename)


# fps = scene.render.fps
# fps_base = scene.render.fps_base
fps = 30


def write_csv(csv_table, csv_file_name):
    with open(csv_file_name, 'w+') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ')
        for csv_row in csv_table:
            csvwriter.writerow(csv_row)


def frame_to_time(frame_number):
    raw_time = (frame_number - 1) / fps
    return int(raw_time)


write_csv(sorted([(label, frame_to_time(marker.frame))
                  for label, marker in scene.timeline_markers.items()],
                 key=lambda t: t[1]),
          stopwatch_filepath)
