from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):

	def test_home_GET(self):
		client = Client()
		response = client.get(reverse('home'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/index.html')

	def test_home_POST(self):
		client = Client()
		response = client.post(reverse('home'), {
			'term' : 'Jack'
			})

	def test_lyrics_GET(self):
		client = Client()
		response = client.get(reverse('lyrics', args=['1']))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/lyrics.html')

	def test_results_GET(self):
		client = Client()
		response = client.get(reverse('results', args=['WAP']))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'groovesweeperapp/results.html')