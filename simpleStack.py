"""This program is and implementation of a simple Stack"""

class Stack:
    stackData = []
    def push(self,val):
        """returns add element to top of Stack"""
        self.stackData.append(val) ##add val to stackData object

    def pop(self):
        """Removes the top element in stack"""
        self.stackData.pop() ##removes the last/top element stack

    def max(self):
        """return the maximum element in Stack"""
        return max(self.stackData) ## returns the Maximum element in Stack

    def __str__(self):
        return "This program is and implementation of a a simple Stack. It has methods " \
               "\npush(); adds value to top of stack, pop(); Removes top value in stack,\nmax(); return maximum element in Stack"

###TEST
T = Stack()
T.push(2)
T.push(5)
T.push(10)
print(T.max())
T.pop()
print(T.max())
print(T)