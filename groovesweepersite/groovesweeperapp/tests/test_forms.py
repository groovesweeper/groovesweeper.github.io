from django.test import SimpleTestCase
from groovesweeperapp.forms import SongQueryForm

class TestForms(SimpleTestCase):

	def test_SongQueryForm_valid(self):
		form = SongQueryForm(data={
			'term': 'test'
			})
		self.assertTrue(form.is_valid())

	def test_SongQueryForm_invalid(self):
		form = SongQueryForm(data={
			'term': 'jrojtfldvdamufxturhcctupztkecuukwoeflysaplwsqbpyktwjkhwtbcswodyzxrpceffwyzqnuawrsbswjiowvyqgzznicbtplm'
			})
		self.assertFalse(form.is_valid())

