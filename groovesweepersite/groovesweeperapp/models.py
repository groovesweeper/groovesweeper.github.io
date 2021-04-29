"""
Stores models, which are the interface Django uses to store data in the database
"""

from django.db import models

# Create your models here.
class SongManager(models.Manager):
    """
    This manager makes it simple to instantiate a SongModel object in views
    """
    def createSong(self, sname, sartist, slyrics, sexplicit, surl, sid):
        song_model = self.create(name=sname, artist=sartist, lyrics=slyrics, \
         explicit_words=sexplicit, url=surl, db_song_id=sid)
        return song_model

class SongModel(models.Model):
    """
    Song Model stores information used to create a song object in the database
    """
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    lyrics = models.TextField()
    explicit_words = models.TextField()
    url = models.CharField(max_length=100)
    db_song_id = models.CharField(max_length=20)

    objects = SongManager()

    def __str__(self):
        return '{} {}'.format(self.name, self.db_song_id)


class SongQueryModel(models.Model):
    """
    This exists so we can extract the term from the Model Form in the home view
    """
    term = models.CharField(max_length=100)
