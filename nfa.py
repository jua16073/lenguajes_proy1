# Generacion de NFA
import trees

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
EPSILON = "ε"

class Automata:
    def __init__(self, exp):
        self.id = exp
        self.states = []

class State:
    def __init__(self, num, num2):
        self.id = num
        self.id2 = num2
        self.transitions = []
        self.accept = False
        #self.transitions.append(Transition(EPSILON, self.id))
    pass

class Transition:
    def __init__(self, sym, to):
        self.symbol = sym
        self.to = to


def post_order(tree):
    symbols = []
    if tree.left != None:
        s = post_order(tree.left)
        for symb in s:
            symbols.append(symb)
    if tree.right != None:
        s = post_order(tree.right)
        for symb in s:
            symbols.append(symb)
    symbols.append(tree.data)
    return symbols