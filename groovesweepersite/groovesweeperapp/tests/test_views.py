from django.test import TestCase, Client
from django.urls import reverse, resolve
from groovesweeperapp.views import homeView, lyricsView, resultsView
import json

class TestViews(TestCase):

	def test_home_GET(self):
		client = Client()
		response = client.get(reverse('home'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')

	def test_home_POST(self):
		client = Client()

		response = client.post('/#')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')

		response = client.post('/mod')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')

		response = client.post('/search-button')
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

	#def test_lyrics_GET(self):
	#	client = Client()
	#	response = client.get(reverse('lyrics', args=[5832126]))
	#	self.assertEquals(response.status_code, 200)
	#	self.assertTemplateUsed(response, 'groovesweeperapp/lyrics.html')

	def test_results_GET(self):
		client = Client()
		response = client.get(reverse('results', args=['WAP']))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/results.html')