#DailyCoding
class AutoCompltSystem:
    def __init__(self, AlphabetSystem):
        self._AlphaSystem = AlphabetSystem #instantiate the alphabet system
        self.lexicon = {}#instantiate dictionary of letter and words
        for character in self._AlphaSystem:#create the dictionary of character keys holding list values
            self.lexicon[character] = []

    def complete(self, Letters, WordList):## take the
        for word in WordList:
            word = word.lower()
            self.lexicon[word[0]].append(word)#append words to list in Lexicon dictionary. words that begin with the same letter as the key
        PontWords = self.lexicon[Letters[0]] ##get the list of probable words
        return [word for word in PontWords if Letters in word] ## return the list of words most likely to be the searched word

##TEST
alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
sys = AutoCompltSystem(alpha)
print(sys.complete("bu", ["Bird", "bull", "Lion", "Crow"]))

"""This is not complete, not up to accepted standard""" ##Can be made better to autocpompolet with two or more letter given.