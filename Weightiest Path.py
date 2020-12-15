'''
You are given an array of arrays of integers,
where each array corresponds to a row in a triangle of numbers.
For example, [[1], [2, 3], [1, 5, 1]]

represents the triangle:

  1
 2 3
1 5 1

We define a path in the triangle to start at the top and go down one row at a time to an adjacent value,
eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

'''

def isWeightiest(array):
    '''return the path with highest value sum'''
    weightiest = 0
    for row in array:##go to each row
        weightiest += max(row) #get the maximum value on that row and increment the weightiest variable
    return weightiest

print(isWeightiest([[1], [2, 3], [1, 5, 1]]))
