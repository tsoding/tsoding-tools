import httplib2
import os
import re
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage

MISSING_CLIENT_SECRETS_MESSAGE = ""
YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"


# TODO(bc02b696-9ad8-4572-8faa-58caed05f612): authorization and credential storage
#
# Develop a mechanism for storing and retrieving credentials for
# ytservice_from_credentials() and authorizing the Tsoding Tools to
# get those credentials in the first place.
#
# For more info see https://developers.google.com/api-client-library/python/guide/aaa_oauth

def ytservice_from_credentials(credentials):
    """Constructs YouTube Service"""
    return build("youtube",
                 "v3",
                 http=credentials.authorize(httplib2.Http()))


# TODO(f2430622-3245-41e3-9761-35b65f40e9fa): implement unlist_playlist_videos()
def unlist_playlist_videos(ytservice, playlist):
    """Unlists all of the videos in a specific playlist using YouTube API.

    Doesn't unlist the playlist itself. Only the videos.
    """
    pass
