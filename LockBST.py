##DailyCoding
class BiNode():
    """define the binary search tree Node"""
    def __init__(self, val, leftChild, rightChild):
        self.val = val ##node val
        self.leftChild = leftChild ##left child of node
        self.rightChild = rightChild ##right child of node
    def insert(self, newVal):
        """Insert Value to the right or left of a BiNode"""
        if newVal < self.val:
            if self.leftChild!=None: self.leftChild.insert(newVal) ##if less than root insert in left subTree
            else: self.leftChild = BiNode(newVal, None, None) #if None object in left subtree creat new BiNode there
        elif newVal > self.val:
            if self.rightChild != None: self.rightChild.insert(newVal)##else insert in right subtree
            else: self.rightChild = BiNode(newVal, None, None)#if None object in right subtree creat new BiNode there
    def isLocked(self, Node):
        """return a boolean val whether a node is locked or not"""
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
        ##if all node in its subtree is locked then The node is Locked
    def unLock(self):
        """Unlocks a BiNode"""
        ##unloced if all the node in its subtree are unlocked