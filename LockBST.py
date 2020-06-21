##DailyCoding
class BiNode():
    """define the binary search tree Node"""
    def __init__(self,val, leftChild, rightChild):
        self.val = val ##node val
        self.leftChild = leftChild ##left child of node
        self.rightChild = rightChild ##right child of node

    def insert(self, newVal):
        """Insert Value to the right or left of a BiNode"""
        if newVal < self.val: self.leftChild.insert(newVal) ##if less than root insert in left subTree
        elif newVal > self.val: self.rightChild.insert(newVal)##else insert in right subtree

class Tree:
    """Simple Binary search Tree"""
    root = None ##instantiate Root of binary Tree
    def inSert(self, val):
        """Add value to Tree"""
        if self.root == None: root = BiNode(val, None, None) ##Add the first element of Tree with null children
        else: ##if tree is not empty
            self.root.insert(val) ##This implements insert Methode in BiNode class
    def isLocked(self):
        """return a bolean val on wether Node is locked"""
    def unLock(self):
        """Unlocks a BiNode"""