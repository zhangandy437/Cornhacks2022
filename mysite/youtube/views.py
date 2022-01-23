from django.http import HttpResponse, response
from . import quickstart, scrape
import os
from moviepy.editor import AudioFileClip, ImageClip, VideoClip, VideoFileClip
from PIL import Image, UnidentifiedImageError

IMG_PATH = 'imgs'

# Create your views here.
def index(request):
    filename = quickstart.downloadrandom()
    file = open(filename, "rb").read()

    response = HttpResponse()
    response.write(file)
    # response['Content-Type'] = 'audio/mp3'
    response['Content-Disposition'] = f'attachment; filename={filename}' 
    quickstart.cleanup(filename)
    return response

def stitch(request):
    # scrap images
    print("--- Getting audio...")
    audio_path = quickstart.downloadrandom()
    audio = AudioFileClip(audio_path)
    
    print('--- Getting images...')
    photos = scrape.get_images_data()
    fphotos = []
    for photo in photos:
        try:
            fphotos.append(Image.open(photo).resize((800,800), Image.ANTIALIAS))
        except UnidentifiedImageError:
            print(end='')
    
    print('--- Making gif...')
    duration = audio.duration // len(fphotos) * 1000
    fphotos[0].save(IMG_PATH + '/temp.gif', save_all=True, append_images=fphotos[1:], duration=duration)
    img = VideoFileClip(IMG_PATH + '/temp.gif')
    
    print('--- Creating vid...')
    vid = img.set_audio(audio)
    vid.duration = audio.duration
    vid.write_videofile("test.mp4", fps=60)
    
    file = open('test.mp4', "rb").read()
    
    response = HttpResponse()
    response.write(file)
    # response['Content-Type'] = 'audio/mp3'
    response['Content-Disposition'] = f'attachment; filename=vid.mp4' 
    # cleanup
    cleanup()
    quickstart.cleanup(audio_path)
    return response

def cleanup(imgs):
    for img in imgs:
        os.remove(img)
    os.remove('test.mp4')