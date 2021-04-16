from django.test import TestCase, SimpleTestCase
from groovesweeperapp.models import SongQueryModel, SongModel
from django.core.exceptions import ValidationError


class TestModels(TestCase):

	def setUp(self):
		self.Song1 = SongModel.objects.create(
			name = 'testSong',
			artist = 'DJ JY',
			lyrics = 'these are some lyrics to this song, shit, sometimes I play ping pong, fuck',
			explicit_words = 'shit fuck',
			url = "somestring"
		)

		self.SongQuery1 = SongQueryModel.objects.create(
			term = 'testTerm'
		)

	def test_SongModel_valid(self):
		model = self.Song1
		self.assertEquals(model.name, 'testSong')
		self.assertEquals(model.artist, 'DJ JY')
		self.assertEquals(model.lyrics, 'these are some lyrics to this song, shit, sometimes I play ping pong, fuck')
		self.assertEquals(model.explicit_words, 'shit fuck')
		self.assertEquals(model.url, 'somestring')
		

	def test_songModel_invalid(self):
		model = self.Song1
		model.name = 'MtnwGnr0OG7huyBplijKrdGMc5sGHgJ23nDduoKAIEuPA2RcKKwaQUb'
		self.assertRaises(ValidationError, model.full_clean)

		model.name = 'testSong'
		model.artist = 'MtnwGnr0OG7huyBplijKrdGMc5sGHgJ23nDduoKAIEuPA2RcKKwaQUb'
		self.assertRaises(ValidationError, model.full_clean)

		model.explicit_words = 'shit fuck'
		model.url = 'xbURNO1Y74LoY9cEGIWhlydB5DOHxhoU3KsalCV639gKPdEAf1MVeSCGEDSmXofvTkxdxvOR0IIsM4XkfnH62r9lLGjp8GsKXM87B'
		self.assertRaises(ValidationError, model.full_clean)

	def test_SongQueryModel_valid(self):
		model = self.SongQuery1
		self.assertEquals(model.term, 'testTerm')

	def test_SongQueryModel_invalid(self):
		model1 = self.SongQuery1
		model1.term = 'Ss6X8lliirCJnowfp3wBMM7rr2m6nwUZWfFntcAy3QdZmdtewyYCWF7onbQ5ohVCJzWG2bpiOO45qvzhw2KzTEmFEZhZr1jTBQ2CJ'
		self.assertRaises(ValidationError, model1.full_clean)





