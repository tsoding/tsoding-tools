### Basic Usage

```console
# from the root of the repo
./venv/bin/ipython
> import youtube
> import config
> ytservice = youtube.ytservice_from_config(config.home_tsoding_config())
> youtube.video_ids_of_playlist(ytservice, '<PLAYLIST_ID>')
```
