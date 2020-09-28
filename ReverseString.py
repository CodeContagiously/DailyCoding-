def ReverseString(list_of_Strings):
    ##another way:
    ## list(map(lambda String: String[::-1], list_of_Strings
    return [String[::-1] for String in list_of_Strings]


# print(ReverseString("sihT si ym tset".split()))