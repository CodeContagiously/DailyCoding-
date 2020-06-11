#DailyCoding
## 
class AutoCompltSystem:
    def __init__(self, AlphabetSystem):
        self._AlphaSystem = AlphabetSystem #instantiate the alphabet system
        self.lexicon = {} #instantiate dictionary of letter and words
        for character in self._AlphaSystem: #create the dictionary of character keys holding list values
            self.lexicon[character] = []

    def complete(self,Letter,WordList):
        for word in WordList:
            word = word.lower()
            self.lexicon[word[0]].append(word) #append words to list in Lexicon dictionary.
        return self.lexicon[Letter] #return List Value in dictionary with key "Letter"

##TEST
alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
sys = AutoCompltSystem(alpha)
print(sys.complete("b",["Bird","bull", "Lion", "Crow"]))

"""This is not complete, not up to accepted standard""" ##Can be made better to autocpompolet with two or more letter given.