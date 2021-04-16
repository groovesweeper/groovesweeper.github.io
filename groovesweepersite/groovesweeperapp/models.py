from django.db import models

# Create your models here.
class SongModel(models.Model):
    # Song Model stores information used to create a song object in the database
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    lyrics = models.TextField()
    explicit_words = models.TextField()
    url = models.CharField(max_length=100)

class SongQueryModel(models.Model):
    # This exists so we can extract the term from the Model Form in the home view
    term = models.CharField(max_length=100)
