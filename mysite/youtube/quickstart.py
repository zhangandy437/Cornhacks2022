from __future__ import unicode_literals
from pyyoutube import Api
from random import random
import youtube_dl
from os import listdir
from os.path import isfile, join
from youtube_dl.utils import DownloadError

api = Api(api_key="AIzaSyDQgrNtKZlwTQbXVy_JbspnqHz-XWyFzX4")

# def downloadmp3():
playlists = api.get_playlist_items(playlist_id="PLWOGZHNCc5NnJox5IaqDSMUmMKRCT7Ao9")

# for item in playlists.items:
#     print(item)
    
# print(playlists.pageInfo)
index = int(random() * len(playlists.items))
item = playlists.items[index]
print(item)



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
        ydl.download(['https://www.youtube.com/watch?v=DvOq4plWHjg&list=PLWOGZHNCc5NnJox5IaqDSMUmMKRCT7Ao9&index=13'])
except DownloadError:
    print("welp")
print('hi')
files = [f for f in listdir('.') if isfile(join('.', f))]
    