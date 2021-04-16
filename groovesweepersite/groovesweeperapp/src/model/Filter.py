class Filter:
	"""
	A Singleton class used to represent the filter used for filtering songs.

	...

	Attributes
	----------
	SEVEN_DIRTY_WORDS : tuple
		Contains seven dirty words for radio. It is a preset filter.
	COMMON_SWEAR_WORDS : tuple
		Contains common swears that users may want to filter. It is a preset
		filter.
	__customFilterWords : set
		Custom words the user may want to filter out.
	__fullFilter : set
		All the words being filtered. The main filter that is used to filter songs.
	__instance : Filter
		The Filter Object itself.

	Methods
	-------
	getInstance() :
		Returns the instance of the Filter Object

	addWord(word) :
		Adds the word to the __customFilterWords and __fullFilter if the word
		is not in the __fullFilter.

	removeWord(word) :
		Removes the word from __fullFilter if the word is in __fullFilterWords
		and removes the word from __customFilterWords if the word is in
		__customFilterWords.

	getSevenDirtyWords() :
		Gets the __SEVEN_DIRTY_WORDS tuple.

	getCommonSwearWords() :
		Gets the __COMMON_SWEAR_WORDS tuple.

	all7():
		Check if __SEVEN_DIRTY_WORDS in __fullFilter

	allCommon():
		Check if __COMMON_SWEAR_WORDS in __fullFilter

	"""
	__instance = None

	def __init__(self):
		"""
		Filter Constructor:
		 	Initializes the Filter object and populates the __fullFilter set.
		"""
		if Filter.__instance != None:
			raise Exception("This class is a singleton! Call getInstance() instead.")
		else:
			self.__customFilterWords = set()
			self.__fullFilter = set()
			self.__SEVEN_DIRTY_WORDS = ("fuck", "shit", "piss", "cunt", "cocksucker", "motherfucker", "tits")
			self.__COMMON_SWEAR_WORDS = ("ass", "dick", "pussy", "bitch")
			for word in self.__SEVEN_DIRTY_WORDS:
				self.__fullFilter.add(word)
			#for word in self.__COMMON_SWEAR_WORDS:
				#self.__fullFilter.add(word)

			Filter.__instance = self

	@staticmethod
	def getInstance():
		"""
		Static access method. Returns the instance of Filter.
		Returns
		-------
		Filter
			the Filter object instance.
		"""
		if Filter.__instance == None:
			Filter()
		return Filter.__instance

	def addWord(self, word):
		"""
		Adds the word to the __customFilterWords and __fullFilter if the word
		is not in the __fullFilter.

		Parameters
		----------
		word : str
			The word to be added.
		Returns
		-------
		boolean
			True if the word was added, False if the word was not added because it
			was already present.
		"""
		if word not in self.__fullFilter:
			self.__customFilterWords.add(word)
			self.__fullFilter.add(word)
			return True
		return False

	def removeWord(self, word):
		"""
		Removes the word from __fullFilter if the word is in __fullFilterWords
		and removes the word from __customFilterWords if the word is in
		__customFilterWords.

		Parameters
		----------
		word : str
			The word to be removed.

		Returns
		-------
		boolean
			True if the word has been removed from all filters. False if the word
			has not been removed because it was not present.
		"""
		removed = False
		if word in self.__customFilterWords:
			self.__customFilterWords.remove(word)
			removed = True
		if word in self.__fullFilter:
			self.__fullFilter.remove(word)
			removed = True
		return removed

	def getSevenDirtyWords(self):
		"""
		Gets the __SEVEN_DIRTY_WORDS tuple
		Returns
		-------
		tuple
			__SEVEN_DIRTY_WORDS
		"""
		return self.__SEVEN_DIRTY_WORDS

	def getCommonSwearWords(self):
		"""
		Gets the __COMMON_SWEAR_WORDS tuple
		Returns
		-------
		tuple
			__COMMON_SWEAR_WORDS
		"""
		return self.__COMMON_SWEAR_WORDS

	def getFullFilter(self):
		"""
		Gets the __fullFilter set

		Returns
		-------
		set
			a deepcopy of the __fullFilter
		"""
		fullFilter = set()
		for word in self.__fullFilter:
			fullFilter.add(word)
		return fullFilter

	def all7(self):
		"""
		Checks if seven dirty words are present in FullFilter

		Returns
		-------
		boolean
			True if all seven words are in FullFilter, otherwise False
		"""
		return set(self.__SEVEN_DIRTY_WORDS).issubset(self.__fullFilter)

	def allCommon(self):
		"""
		Checks if common swear words are present in FullFilter

		Returns
		-------
		boolean
			True if all common swears are in FullFilter, otherwise False
		"""
		return set(self.__COMMON_SWEAR_WORDS).issubset(self.__fullFilter)
