from Filter import Filter

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
    __lyrics : list of strings
        Contains all words in the song lyrics
    __explicitWords : set
        Contains one of each explicit word found in song lyrics
    __url : string
        Link to the song lyrics on Genius website

    Methods
    -------
    getName() :
        Returns song name
    getArtist() :
        Returns artist name
    getExplicitWords() :
        Gets the explicit words in the song.
    getNumOfExplicitWords() :
        Returns the number of explicit words in the song.
    isExplicit() :
        If __explicitWords contains words, returns True indicating the song is
		not clean. Otherwise, false.
    filterSong() :
        Filters a song for explicit words and adds those words to __explicitWords.
		When using this function, you can assume that it is the first time
		filtering the song and explicitWords set will be empty.


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
        self.filterSong()

    def getName(self):
        """
        Returns
        -------
            Name of song.
        """
        return self.__name

    def getArtist(self):
        """
        Returns
        -------
            Name of artist.
        """
        return self.__artist

    def getExplicitWords(self):
        """
        Gets the set of explicit words in the song.

        Returns
        -------
        set
			A deep copy of the __explicitWords set
        """
        explicit = set()
        for word in self.__explicitWords:
            explicit.add(word)

        return explicit

    def getNumOfExplicitWords(self):
        """
		Gets the number of explicit words in the song.

        Returns
        -------
        int
            Number of words in __explicitWords
        """
        return len(self.__explicitWords)

    def isExplicit(self):
        """
        If __explicitWords is not empty, the song instance is considered explicit.
        Returns
        -------
        boolean
            True if __explicitWords is not empty.
            False, otherwise.
        """
        if len(self.__explicitWords) > 0:
            return True
        return False

    def filterSong(self):
        """
        Filters a song for explicit words and adds those words to __explicitWords.
		When using this function, you can assume that it is the first time
		filtering the song and explicitWords set will be empty.
        Returns
        -------
            None
        """
        self.__explicitWords = set()
        filter = Filter.getInstance()
        fullFilter = filter.getFullFilter()
        for word in self.__lyrics:
            if word in fullFilter:
                self.__explicitWords.add(word)
        return

if __name__ == '__main__':
	# testing to see there is no rep exposure
	song = Song(["ass", "piss", "Hello"], "Me", "test", "www.test.com")
	print(song.isExplicit())
	explicitWords = song.getExplicitWords()
	print(explicitWords)
	explicitWords.remove("piss")
	explicitWords2 = song.getExplicitWords()
	print(explicitWords2)
