from django.db import models

# Create your models here.
class SongModel(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    lyrics = models.TextField(max_length=2500)
    explicit_words = models.TextField(max_length=150)
    url = models.CharField(max_length=100)

class SongQueryModel(models.Model):
    term = models.CharField(max_length=100)
