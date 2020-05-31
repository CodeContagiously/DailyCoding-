##Daily Coding..
##

def main(A):
    ##product array: return new Array with every ith index being a value of productt
    ##of other elements excluding the index.
    ##example: given [3,2,1] ---> [2,3,6]
    ##complexity O(n*k)
    products = []
    for i in range(len(A)):
        result=1
        print("ith element", i)
        for n in A[:i]+ A[i+1:]:
            print("n", n)
            result *= n
            print("result",result)
        products.append(result)
    print(products)
        
main([3,2,1])
