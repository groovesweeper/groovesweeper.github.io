class Filter:
    # Filters that should not be changed by the user.
    SEVEN_DIRTY_WORDS = ("fuck", "shit", "piss", "cunt", "cocksucker", "motherfucker", "tits")
    COMMON_SWEAR_WORDS = ("ass", "dick", "pussy", "bitch")
    # Filter that can be changed by the user
    __customFilterWords = set()
    # fullFilter is all current filtered words
    __fullFilter = set()
    # Filter is a singleton class so it should have a ref to itself
    __instance = None

    def __init__(self):
        if Filter.__instance is not None:
            raise Exception("This class is a singleton! Call getInstance() instead.")
        else:
            for word in self.SEVEN_DIRTY_WORDS:
                Filter.__fullFilter.add(word)
            for word in self.COMMON_SWEAR_WORDS:
                Filter.__fullFilter.add(word)
            Filter.__instance = self

    @staticmethod
    def getInstance():
        if Filter.__instance is None:
            Filter()
        return Filter.__instance

    def addWord(word):
        # TODO Implement
        return False

    def removeWord(word):
        # TODO Implement
        return

    def filteredWords():
        # I figured this would be a useful function to print out all
        # words in __fullFilter

        # TODO Implement
        return

    print("test")
