def SquareSortedList(list_of_number):
    new_list = [num*num for num in list_of_number]
    ##other methods
    ##new_list = List(map(lamda x: x*x, list_of_number))
    ##
    new_list.sort()
    return new_list
##SquareSortedList([1,2,3,6])