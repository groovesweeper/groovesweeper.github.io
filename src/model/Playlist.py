from Filter import *
from Song import *
import copy


class Playlist:
	"""
	A class used to represent playlists holding multiple songs
	...

	Attributes
	----------
	__songList: List
		List of all songs in a playlist
	__name: String
		Name of the playlist
	__numOfExplicit
		Number of explicit songs in the playlist

	Methods
	-------
	getSongs() :
		Gets the list of songs in the current playlist
	isExplicit() :
		Returns true if any song in the playlist is explicit, returns false
		otherwise. Also increments __numOfExplicit.
	getCleanPlaylist() :
		Creates a copy of the current playlist and removes all explicit songs.
		Returns that new clean playlist.
	reFilterSongs() :
		Refilters all songs in the current playlist by calling filterSong in
		Song class

	"""

	__songList = list()
	__name = ""
	__numOfExplicit = 0

	def __init__(self, songList, name):
		"""
		Playlist constructor:
			Initializes the playlist object and populates __songList and __name
		"""
		self.__songList = songList
		self.__name = name

	def getSongs(self):
		"""
		Gets the list of songs in the current playlist

		Returns
		-------
		list
			__songList
		"""
		return copy.deepcopy(self.__songList)

	def isExplicit(self):
		"""
		Returns true if any song in the playlist is explicit, returns false
		otherwise. Also increments __numOfExplicit.

		Returns
		-------
		boolean
			True if any song is explicit, false otherwise.
		"""
		explicit = False
		for song in self.__songList:
			if song.isExplicit():
				self.__numOfExplicit += 1
				explicit = True
		return explicit

	def getCleanPlaylist(self):
		"""
		Creates a copy of the current playlist and removes all explicit songs.
		Returns that new clean playlist.

		Returns
		-------
		Playlist object
			Returns a copy of the current playlist, excluding any explicit songs.
		"""

		cleanSongList = self.getSongs()
		anyExplicit = False
		for song in cleanSongList:
			if song.isExplicit():
				cleanSongList.remove(song)
				anyExplicit = True
		if anyExplicit:
			cleanPlayList = Playlist(cleanSongList, self.__name)
			return cleanPlayList
		else:
			return self

	def reFilterSongs(self):
		"""
		Refilters all songs in the current playlist by calling filterSong in
		Song class
		"""
		for song in self.__songList:
			Song.Song.filterSong(Filter.getInstance())

if __name__ == '__main__':
	# testing all functions
	s1 = Song("ass piss Hello", "Me", "test", "www.test.com")
	s2 = Song("clean song", "Me", "Clean song test", "www.test.com")
	playlist = Playlist([s1, s2], "test")
	print(playlist.isExplicit())
	cleanList = playlist.getCleanPlaylist()
	print("cleanlist length should be 1: " + str(len(cleanList.getSongs()) == 1))
	print("Playlist length should still be 2: " + str(len(playlist.getSongs()) == 2))
