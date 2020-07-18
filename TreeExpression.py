from LockBST import BiNode ##import binary node class from LockBST module

class Eval:
    solution = None ##not needed
    def __init__(self,TreeExp):
        self.exp = TreeExp ##get tree expression as an instance for the class

    def eval(self):
        if type(self.exp.rightChild)!= str: ##if right Child is an int, so is left (Tree is a balanced)
            return eval(str(self.exp.rightChild) + self.exp.val + str(self.exp.leftChild))
        else:
            return eval(str(self.exp.lefttChild.eval)+self.exp.val + str(self.exp.rightChild.eval))

####TEST..



