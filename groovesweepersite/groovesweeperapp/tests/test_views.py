from django.test import TestCase, Client
from django.urls import reverse, resolve
from groovesweeperapp.views import homeView, lyricsView, resultsView
import json
"""
Test cases for all views contained in the app. Specifically testing to make sure each page uses the correct code
and templates for that page.
"""
class TestViews(TestCase):
	"""
	Testing the home page can be accesses correctly with the correct html template
	"""
	def test_home_GET(self):
		client = Client()
		response = client.get(reverse('home'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')
	"""
	Even though this is a post and usually posts return a 302 for a redirect, since all
	the filter functions refresh the same page, the response returns a 200 status code 
	"""
	def test_home_POST_filter(self):
		client = Client()

		response = client.post('/#')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')

		response = client.post('/mod')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')

		response = client.post('/add-7')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')

		response = client.post('/add-common')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')

		response = client.post('/add-custom')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')
	"""
	Testing the results page can be accessed correctly with the correct song that is searched for
	and the correct html template
	"""
	def test_results_GET(self):
		client = Client()
		response = client.get(reverse('results', args=['WAP']))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/results.html')
	"""
	Testing the lyrics page can be accessed correctly. First have to go through the results page to set up the 
	songs in the db, then access the specific results page for the specific song by its song_id
	"""
	def test_lyrics_GET(self):
		client = Client()
		response = client.get(reverse('results', args=['WAP']))
		response = client.get(reverse('lyrics', args=[5832126]))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/lyrics.html')