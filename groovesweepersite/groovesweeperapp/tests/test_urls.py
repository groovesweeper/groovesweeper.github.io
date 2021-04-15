from django.test import SimpleTestCase
from django.urls import reverse, resolve
from groovesweeperapp.views import home, lyrics, results

class TestUrls(SimpleTestCase):

	def test_home_url_is_resolved(self):
		url = reverse('home')
		print(resolve(url))
		self.assertEquals(resolve(url).func, home)

	def test_lyrics_url_is_resolved(self):
		url = reverse('lyrics')
		self.assertEquals(resolve(url).func, lyrics)

	def test_results_url_is_resolved(self):
		url = reverse('results')
		self.assertEquals(resolve(url).func, results)
