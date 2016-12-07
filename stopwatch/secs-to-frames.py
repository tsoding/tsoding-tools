#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

def read_csv(csv_file_name):
    with open(csv_file_name, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ' ')
        return [[comment, int(secs)] for [comment, secs] in csvreader]

def save_csv(table, csv_file_name):
    with open(csv_file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ' ')
        for row in table:
            csvwriter.writerow(row)

def secs_to_frames(table, fps):
    return [[comment, secs * fps] for [comment, secs] in table]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage: ./secs-to-frames.py <stopwatch-log> <fps>"
        exit(1)

    csv_file_name = sys.argv[1]
    fps = int(sys.argv[2])
    save_csv(secs_to_frames(read_csv(csv_file_name), fps),
             "%s.%dfps" % (csv_file_name, fps))

