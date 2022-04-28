from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length= 100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    likes = models.IntegerField()
    album_image = models.CharField(max_length=500)

    