def SplitString(string,k):
    maxLen = [len(word) for word in string.split()]##get the length of longest word in the string
    if maxLen > k: return None ##return Null object if a word in string can't be split to size K
    ##else
    SplitList =[]##instantiate the splitList
    words = string.split() ##create an array of words in string
    # for indx in range(len(words)):
    indx=0
    word = words[indx]
    if len(word)<k:##
        while True:
            indx+=1
            word += " "+words[indx] ##increase length of word by adding more substrings to it
            if len(word)==k:
                SplitList.append(word)
                break ##exit loop
            if len(word)>k:
                word = word[:word.rfind(" ")+1]

    else:
        ##else add word to SplitList because its length <= K
        SplitList.append(words[indx])
            
          ##Incomplete!!!