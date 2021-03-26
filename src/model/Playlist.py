from __init__ import *
from Filter import *
from main import *
from Song import *
import copy


class Playlist:
	"""
	A class used to represent playlists holding multiple songs
	...

	Attributes
	----------
	_songList: List
		List of all songs in a playlist
	_name: String
		Name of the playlist
	_numOfExplicit
		Number of explicit songs in the playlist

	Methods
	-------
	getSongs() :
		returns the list of songs in the current playlist
	isExplicit() :
		returns true if any song in the playlist is explicit, returns false otherwise. Also increments
		_numOfExplicit.
	getCleanPlaylist() :
		creates a copy of the current playlist and removes all explicit songs. Returns that new clean playlist.
	reFilterSongs() :
		re filters all songs in the current playlist by calling filterSong in Song class

	"""
    
    _songList = list()
    _name = ""
    _numOfExplicit = 0

    def __init__(self, songList, name):
    	"""
		Playlist constructor:
			Initializes the playlist object and populates _songList and _name
    	"""
        self._songList = songList
        self._name = name

    def getSongs(self):
    	"""
		returns the list of songs in the current playlist
		Returns
		-------
		list
			_songList
    	"""
        return self._songList

    def isExplicit(self):
    	"""
		returns true if any song in the playlist is explicit, returns false otherwise. Also increments
		_numOfExplicit.
		Returns
		-------
		boolean
			True if any song is explicit, false otherwise.
    	"""
        explicit = False
        for song in self.getSongs():
            if song.isExplicit():
                self._numOfExplicit += 1
                explicit = True
        return explicit

    def getCleanPlaylist(self):
    	"""
		creates a copy of the current playlist and removes all explicit songs. Returns that new clean playlist.
		Returns
		-------
		Playlist object
			returns the copy of the current playlist, excluding any 
    	"""
        # creates a copy of the current playlist and removes all explicit songs. Returns that new clean playlist.
        cleanPlaylist = copy.deepcopy(self)
        cleanSongList = cleanPlaylist.getSongs()
        anyExplicit = False 
        for song in cleanSongList:
            if song.isExplicit():
                cleanSongList.remove(song)
                anyExplicit = True
        if anyExplicit:
        	return cleanPlaylist
        else:
        	return self

    def reFilterSongs(self):
    	"""
		re filters all songs in the current playlist by calling filterSong in Song class
    	"""
        for song in self.getSongs():
            Song.Song.filterSong(Filter.getInstance())
