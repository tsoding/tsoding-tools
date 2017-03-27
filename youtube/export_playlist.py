#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def usage():
    print "./export_playlist.py <playlist-id> <output.json>"


# TODO(d3df8ae8-d0ea-4d94-8562-ad50becdfd52): implement Playlist class
class Playlist(object):
    def __init__(self, playlist_id):
        print "Playlist ID:", playlist_id

    def export_json_to(self, json_file_path):
        print "Output file:", json_file_path


if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        exit(1)

    playlist_id = sys.argv[1]
    output_file_path = sys.argv[2]

    Playlist(playlist_id).export_json_to(output_file_path)
