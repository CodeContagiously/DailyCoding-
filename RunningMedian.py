"""this program computes the running median of a stream of numbers
that is given a stream [2,1,5,7,2,0,5] --> [2,1.5,2,3.5,2,2,2]"""
##Methode 1
def main(array):
    values = [] ##initialise the variable for collecting stream of values
    for Indx in range(len(array)):
        values.append(array[Indx]) ##get the consecutive stream of values
        size = len(values)
        if size>1:
            if size%2!=0: ##if NOT even number of values in list
                median = values[size//2] ##for odd number of elements in list get middle value as median.
                print(median)
            else:
                # print(values)
                median = (values[size//2] + values[size//2 - 1])/2
                print(median)
        else:print(values[0])
main([2,1,5,7,2,0,5])

'''Right, but solving the wrong problem'''