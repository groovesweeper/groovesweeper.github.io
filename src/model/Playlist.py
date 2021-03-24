from __init__ import *
from Filter import *
from main import *
from Song import *
import copy

class Playlist:
	#List of all songs in a playlist
	_songList = list()
	#Name of the playlist
	_name = ""
	#Number of explicit songs in the playlist
	_numOfExplicit = 0

	def __init__(self, songList, name):
		self._songList = songList
		self._name = name

	def getSongs(self):
		# returns the list of songs in the current playlist
		return self._songList

	def isExplicit(self):
		#returns true if any song in the playlist is explicit, returns false otherwise
		explicit = False
		for song in self.getSongs():
			if song.isExplicit():
				self._numOfExplicit+=1
				explicit = True
		return explicit

	def getCleanPlaylist(self):
		#creates a copy of the current playlist and removes all explicit songs. Returns that new clean playlist.
		cleanPlaylist = copy.deepcopy(self)
		cleanSongList = cleanPlaylist.getSongs()
		for song in cleanSongList:
			if song.isExplicit():
				cleanSongList.remove(song)
		return cleanPlaylist

	def reFilterSongs(self):
		#re filters all songs in the current playlist by calling filterSong in Song class
		for song in self.getSongs():
			Song.Song.filterSong(Filter.getInstance())

