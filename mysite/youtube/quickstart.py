from __future__ import unicode_literals
from pyyoutube import Api
from random import random
import youtube_dl
from os import listdir, remove
from os.path import isfile, join
from youtube_dl.utils import DownloadError

api = Api(api_key="AIzaSyDQgrNtKZlwTQbXVy_JbspnqHz-XWyFzX4")

def downloadrandom():
    playlists = api.get_playlist_items(playlist_id="PLWOGZHNCc5NnJox5IaqDSMUmMKRCT7Ao9")

    # for item in playlists.items:
    #     print(item)
        
    # print(playlists.pageInfo)
    index = int(random() * len(playlists.items))
    item = playlists.items[index].contentDetails.videoId
    # https://www.youtube.com/watch?v=  list=PLWOGZHNCc5NnJox5IaqDSMUmMKRCT7Ao9

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print(ydl.download([f'https://www.youtube.com/watch?v={item}']))
    except DownloadError:
        print("welp")

    files = [f for f in listdir('.') if isfile(join('.', f)) and f.endswith('.mp3')]
    return files[0]

def cleanup(file):
    remove(file)
    
# https://www.youtube.com/watch?v=gtl1S0kUMEw&list=PLWOGZHNCc5NnJox5IaqDSMUmMKRCT7Ao9&index=1