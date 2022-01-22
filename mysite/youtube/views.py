from django.http import HttpResponse, response

from . import quickstart

import os


# Create your views here.
def index(request):
    filename = quickstart.downloadrandom()
    file = open(filename, "rb").read()
    # return FileResponse(file)
    # file = open("/path/to/your/song.mp3", "rb").read() 
    response = HttpResponse()
    response.write(file)
    # response['Content-Type'] = 'audio/mp3'
    response['Content-Disposition'] = f'attachment; filename={filename}' 
    quickstart.cleanup(filename)
    return response