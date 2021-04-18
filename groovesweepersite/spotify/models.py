from django.db import models

# this is to store the tokens for a User

class SpotifyToken(models.Model):
	user = models.CharField(max_length=50, unique = True)
	created_at = models.DateTimeField(auto_now_add = True)
	refresh_token = models.CharField(max_length = 150)
	access_token = models.CharField(max_length = 150)
	expires_in = models.DateTimeField()
	token_type = models.CharField(max_length = 50)
