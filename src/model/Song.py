from __init__ import *
from Filter import *
from main import *
from Playlist import *


class Song:
    """
    A class used to determine whether or not a song is explicit or not

    ...

    Attributes
    ----------
    __name : string
        Name of the song being checked for explicit words
    __artist : string
        Songs from this artist are checked for explicit words
    __lyrics : list
        Contains all words in the song lyrics
    __explicitWords : set
        Contains one of each explicit word found in song lyrics
    __url : string
        Link to the song lyrics?

    Methods
    -------
    getName() :
        returns song name
    getArtist() :
        returns artist name
    ExplicitWords() :
        Checks each word in __lyrics. If that word is also in __explicitWords, it is added to a set. Set is returned.
    getNumOfExplicitWords() :
        Returns the length of __explicitWords
    isExplicit() :
        If __explicitWords contains words, returns True indicating the song is not clean. Otherwise, false.
    filterSong() :
        Adds words from Filter.getInstance() to __explicitWords set.

    """
    __name = str()
    __artist = str()
    __lyrics = list()
    __explicitWords = set()
    __url = str()

    def __init__(self, lyrics, artist, name, url):
        """
        Initializes variables used in following methods
        """
        self.__lyrics = lyrics
        self.__artist = artist
        self.__name = name
        self.__url = url

    def getName(self):
        """
        Returns
        -------
            Name of song as instance
        """
        return self.__name

    def getArtist(self):
        """
        Returns
        -------
            Name of artist as instance
        """
        return self.__artist

    def ExplicitWords(self):
        """
        Adds explicit words from __lyrics to set if found in __explicitWords
        Returns
        -------
        set
            A set of explicit words from song is returned.
            If none, empty set is returned.
        """
        explicit = set()
        for word in self.__lyrics:
            if word in self.__explicitWords:
                explicit.add(word)
                return explicit
        return explicit

    def getNumOfExplicitWords(self):
        """
        Returns
        -------
        int
            Number of words in __explicitWords
        """
        return len(self.__explicitWords)

    def isExplicit(self):
        """
        If words populate __explicitWords, the song instance is considered explicit
        Returns
        -------
        bool
            True if __explicitWords is not empty.
            False, otherwise.
        """
        if len(self.__explicitWords) >= 1:
            return True
        return False

    def filterSong(self):
        """
        Checks if words in lyrics are also in Filter.getInstance().
        Adds those words to __explicitWords.
        Returns
        -------
            None
        """
        for word in self.__lyrics:
            if word in Filter.getInstance():
                self.__explicitWords.add(word)
        return
