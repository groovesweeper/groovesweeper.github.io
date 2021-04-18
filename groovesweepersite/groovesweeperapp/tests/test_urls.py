from django.test import SimpleTestCase
from django.urls import reverse, resolve
from groovesweeperapp.views import homeView, lyricsView, resultsView

class TestUrls(SimpleTestCase):

	def test_home_url_is_resolved(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, homeView)

	def test_lyrics_url_is_resolved(self):
		url = reverse('lyrics', args=['1'])
		self.assertEquals(resolve(url).func, lyricsView)

	def test_results_url_is_resolved(self):
		url = reverse('results', args=['WAP'])
		self.assertEquals(resolve(url).func, resultsView)

	def test_homeMod_is_resolved(self):
		url = reverse('home-mod', args=['mod'])
		self.assertEquals(resolve(url).func, homeView)
		

