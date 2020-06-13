#DailyCoding
##
##We use a Linked Data Structure

class Node:
    '''Node Object'''
    def __init__(self, val, nextVal):
        self.val = val
        self.nextVal = nextVal

class LinkedList:
    """Simple LinkedList Data Structure"""
    def __init__(self):
        self.previous, self.current = None, None #instantiate current and previous Nodes
        self.head, self.tail = None, None ##instantiate head and tail as null Values
    def add(self,val):
        """Add val to List"""
        if self.head == None: #if linked List is empty
            self.previous = Node(val,self.tail) #append first element in list
            self.current = self.previous   #set current equal to first element; previous
            self.head = Node(None,self.previous) #redefine Val of Head Variable to reference previous Node
        ##Otherwise if list is not empty
        elif self.current.nextVal == self.tail: self.current.nextVal = Node(val,self.tail) #add new value to end of Linked DataSet
        else: ##else, update the value of current to the last nonempty Node
            while self.current.nextVal != self.tail: self.current = self.current.nextVal
            self.current.nextVal = Node(val, self.tail) ##append new val to end of list
    def isEmpty(self):
        """Evaluate if List is Empty or Not"""
        if self.head is None: return True
        return False
    def get(self,ith_val):
        """Return ith val in list"""
        if self.isEmpty(): return None #return None Object if list is Empty
        self.current,ithVal = self.previous, 1 ##set current to first value in list. So ithVal is at 1
        while ithVal != ith_val:
            self.current = self.current.nextVal
            ithVal+=1
        return self.current.val


class WebLog:
    """Log for Web order"""
    def __init__(self):
        self.__log = LinkedList() #instantiate the log dataSet
    def record(self,order_id):
        '''add order id to log'''
        self.__log.add(order_id)

    def get_Last(self,ithOrder):
        """return the ith order in List"""
        return self.__log.get(ithOrder)

###Test
orders = WebLog()
for num in range(10,21): orders.record(num)
print(orders.get_Last(4))
print(orders.get_Last(10))

"""Successful: modify Later"""