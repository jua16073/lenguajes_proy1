#Para hacer trees

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
    
    def PrintTree(self):
        print(self.data)