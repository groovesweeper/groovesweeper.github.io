from django.test import SimpleTestCase
from groovesweeperapp.forms import SongQueryForm, FilterForm
from django import forms

"""
Testing the models. Making sure thta validation on sizes and data types work as expected.
"""
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

	def test_FilterForm(self):
		form = FilterForm(data={
			'to_add': 'words'
			})
		self.assertTrue(form.is_valid())

