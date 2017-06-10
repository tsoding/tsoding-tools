import httplib2
import sys

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

from functional import arrow
from functools import partial


def clean_kwargs(**kwargs):
    return {
        key: value
        for key, value in kwargs.iteritems()
        if value is not None
    }


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


def playlist_video_page(ytservice, playlist_id, page_token):
    return ytservice.playlistItems().list(
        **clean_kwargs(
            part='snippet',
            maxResults=50,
            playlistId=playlist_id,
            pageToken=page_token
        )
    ).execute()


def collect_all_pages(next_page):
    current_page = next_page(None)
    yield current_page

    while 'nextPageToken' in current_page:
        current_page = next_page(current_page['nextPageToken'])
        yield current_page


def video_pages_as_id_list(video_pages):
    return [item['snippet']['resourceId']['videoId']
            for page in video_pages
            for item in page['items']]


def video_ids_of_playlist(ytservice, playlist_id):
    return video_pages_as_id_list(
        collect_all_pages(
            partial(
                playlist_video_page,
                ytservice,
                playlist_id
            )
        )
    )


def unlist_video(ytservice, video_id):
    return ytservice.videos().update(
        body={
            'id': video_id,
            'status': {
                'privacyStatus': 'unlisted'
            }
        },
        part='status'
    ).execute()


def unlist_playlist_videos(ytservice, playlist_id):
    """Unlists all of the videos in a specific playlist using YouTube API.

    Doesn't unlist the playlist itself. Only the videos.
    """
    return map(partial(unlist_video, ytservice),
               video_ids_of_playlist(ytservice, playlist_id))
