"""This program computes the power set given a set of elements"""

## METHODE  ONE
def PowSet(Set): ##Set is a list object
    """return the power set of the given set of elements"""
    powSet = [[],Set] #intialise the power set with the empty set and the set itself
    powSet = [[item] for item in Set] #add every element in given set as subset in power set
    size = len(Set)  #initialize length of Set
    for indx in range(len(Set)):
        while True:
            if not(Set[indx:indx+2] in powSet): break ##indx + 1!= len(Set) and not(
            powSet.append(Set[indx:size]) ##
            size = size-1 ##decrement size
    return powSet

print(PowSet([1,2,3]))

"""This is a working Progress"""