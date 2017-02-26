# Stolen and adapted from http://blenderscripting.blogspot.ru/2013/06/keyframes-and-timeline-markers.html
import bpy
import csv

scene = bpy.context.scene

# fps = scene.render.fps
# fps_base = scene.render.fps_base
fps = 20


def write_csv(csv_table, csv_file_name):
    with open(csv_file_name, 'w+') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ')
        for csv_row in csv_table:
            csvwriter.writerow(csv_row)


def frame_to_time(frame_number):
    raw_time = (frame_number - 1) / fps
    return int(raw_time)


write_csv([(label, frame_to_time(marker.frame))
           for label, marker in scene.timeline_markers.items()],
          "stopwatch.csv")
