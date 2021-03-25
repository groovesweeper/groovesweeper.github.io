from __init__ import *
from Filter import *
from main import *
from Playlist import *
import sys


class Song:
    # Name of the song query as a string
    __name = str()
    # Name of the artist query as a string
    __artist = str()
    # List of all strings in a song
    __lyrics = list()
    # Set of all filtered explicit words in the song
    __explicitWords = set()
    # URL of the song?
    __url = str()

    """
    If the song or artist lists are not empty a query is initiated.
    If the song or artist lists are empty, the user is asked to query.
    If an artist is queried, user chooses a song from the list to query.
    """

    def __init__(self, lyrics, artist, name, url):
        self.__lyrics = lyrics
        self.__artist = artist
        self.__name = name
        self.__url = url

    # file of selected song is returned as a list of strings
    @staticmethod
    def __parseLyrics(self, __lyrics):
        """
        original_stdout = sys.stdout
        with open('lyrics.txt', 'w') as f:
            sys.stdout = f
            print(genius.lyrics("happy", "pharrell"))
            sys.stdout = original_stdout
        # get full output of lyrics???
        # for line in file:
        # eliminate punctuation
        # parse by space
        # append words to a list
        """
        return self.__lyrics

    @staticmethod
    # asks user to input a song name
    def getName(self):
        """
        if Song.__name is None:
            song_name = input("Enter a song name: ").strip()
            Song.__name.append(song_name)
        else:
            Song()
        """
        return self.__name

    @staticmethod
    # asks user to input an artist name
    def getArtist(self):
        """
        if Song.__artist is None:
            artist_name = input("Enter an artist name: ").strip()
            Song.__artist.append(artist_name)
        else:
            Song()
        """
        return self.__artist

    # Finds explicit words in "__parseLyrics" based on Filter class; adds to __explicitWords
    def ExplicitWords(self, ):
        """
        for words in self.__lyrics:

        return self.__explicitWords
        """

    # Returns count of _explicitWords
    def getNumOfExplicitWords(self):
        num = 0
        num = len(self.__explicitWords)
        return num

    # Returns True if _explicitWords set is not empty; else False
    def isExplicit(self):
        """
        explicit = False
        for song in self.
            if
        """
        return

    # Returns instance of filtered word if found in __parseLyrics
    def filterSong(self, _instance):
        # TODO something
        return

