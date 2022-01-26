import random


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> word = WordFinder('words.txt')
    9 words read
    >>> word.random() in word.words
    True
    >>> word = SpecialWordFinder('words.txt')
    4 words read
    >>> word.random() in word.words
    True
    
    
    """

    def __init__(self, file_path, nomsg = False):

        file = open(file_path)
        """Comprehension for list recommended"""
        self.words = [line.strip() for line in file]

        file.close()
        
        self.file_msg = f"{len(self.words)} words read"
        if not nomsg:
            print(self.file_msg)

    def random(self):
        """Return one random word"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """A version of WordFinder which excludes comments and blank line"""

    def __init__(self, file_path):
        super().__init__(file_path, True)
        self.words = [word for word in self.words
            if not word.startswith('#') and word != '']
        
        print(f"{len(self.words)} words read")
