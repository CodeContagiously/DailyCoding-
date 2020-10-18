"""Reducible question (medium)
A word is defined to be “reducible” if you can remove one letter at a time and get another valid word at each step until you have a one letter word.

Write a function that takes a string as input and returns true if and only if the word is reducible.

Examples:
IsReducible(“sprint”) -> True
“sprint” is reducible since there exists the chain of valid words:
SPRINT
PRINT
PINT
PIT
IT
I

IsReducible(“hiybbprqag”) -> False
“hiybbprqag” is not reducible since it is not a valid word.

PORT  → ORT, PRT, POT, POR
POT
PO, OT, PT  → False

"""
import json
data = json.load(open("Dictionary.txt"))

def isReducible(word):
    word = word.lower()##set all words to lowercase
    if (not word in data): return False ##invalids words are irreducible
    if not("a" in word or "i" in word): return False #words without letters "a","i" can not be reduced
    for i in range(len(word)):#Loop through word ommiting a letter to find a reducible new word 
        newWord = word[:i] + word[i+1:]##
        if(newWord in data):return isReducible(newWord)#if newWord is valid proceed to reducing it for a chain of reducible words
    return True ##word has been reduced to a single valid string. hence return true.
