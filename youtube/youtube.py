import httplib2
import os
import re
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

from functional import arrow


# TODO(#20): document how to retrieve the client secrets file
def flow_from_config(tsoding_config):
    return flow_from_clientsecrets(
        tsoding_config['youtube']['client_secrets_file'],
        scope="https://www.googleapis.com/auth/youtube"
    )


def credentials_from_flow(flow):
    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)

    return credentials


def ytservice_from_credentials(credentials):
    """Constructs YouTube Service from Credentials"""
    return build("youtube",
                 "v3",
                 http=credentials.authorize(httplib2.Http()))


def ytservice_from_config(tsoding_config):
    """Constructs YouTube Service from Tsoding Config"""
    return arrow(tsoding_config,
                 flow_from_config,
                 credentials_from_flow,
                 ytservice_from_credentials)


# TODO(f2430622-3245-41e3-9761-35b65f40e9fa): implement unlist_playlist_videos()
def unlist_playlist_videos(ytservice, playlist):
    """Unlists all of the videos in a specific playlist using YouTube API.

    Doesn't unlist the playlist itself. Only the videos.
    """
    pass
