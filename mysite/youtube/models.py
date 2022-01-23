from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=64)
    audio_file = models.FileField()
    
