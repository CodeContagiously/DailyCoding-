def SegArray(array):
    """return segregated array in order "R", "G", "B"
    example [G,G,R,B] ---> [R,G,G,B]"""
    ##Easy way:  array.sort(reverse=True)  ##but we don't want to use inbuilt func
    array.sort(reverse = True)
    return array

##TEST
print(SegArray(["G","G","B","B","R","R"]))