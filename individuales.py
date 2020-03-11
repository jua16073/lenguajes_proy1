# Para automatas de funciones individuales
import nfa

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']

EPSILON = "ε"

global_counter = 0

def t_handler(tree, automata):
    start = 0
    finish = 0
    if tree.data in OPERATORS:
        if tree.data == ".":
            start , finish = concatenation(tree, automata)
        elif tree.data == "|":
            start, finish = option(tree, automata)
        elif tree.data == "*":
            start, finish = kleene(tree, automata)
    else:
        start, finish = single(tree, automata)
    return start, finish
    pass

def concatenation(tree, automata):
    symbol = tree.data
    
    if tree.left.data in OPERATORS:
        st1, fn1 = t_handler(tree.left, automata)
    else:
        st1, fn1 = single(tree.left, automata)
    
    if tree.right.data in OPERATORS:
        st2, fn2 = t_handler(tree.right, automata)
    else:
        st2, fn2 = single(tree.right, automata)

    fn1.transitions.append(nfa.Transition(EPSILON, st2.id))

    return st1, fn2

def option(tree, automata):
    symbol = tree.data

    start = nfa.State(len(automata.states))
    automata.states.append(start)

    if tree.left.data in OPERATORS:
        st1, fn1 = t_handler(tree.left, automata)
    else:
        st1, fn1 = single(tree.left, automata)
    
    if tree.right.data in OPERATORS:
        st2, fn2 = t_handler(tree.right, automata)
    else:
        st2, fn2 = single(tree.right, automata)
    
    end = nfa.State(len(automata.states))
    automata.states.append(end)

    start.transitions.append(nfa.Transition(EPSILON, st1.id))
    start.transitions.append(nfa.Transition(EPSILON, st2.id))
    fn1.transitions.append(nfa.Transition(EPSILON, end.id))
    fn2.transitions.append(nfa.Transition(EPSILON, end.id))

    return start, end

def kleene(tree, automata):
    symbol = tree.data

    start = nfa.State(len(automata.states))
    automata.states.append(start)

    if tree.left.data in OPERATORS:
        st1, fn1 = t_handler(tree.left, automata)
    else:
        st1, fn1 = single(tree.left, automata)
    
    end = nfa.State(len(automata.states))
    automata.states.append(end)

    start.transitions.append(nfa.Transition(EPSILON, st1.id))
    start.transitions.append(nfa.Transition(EPSILON, end.id))
    fn1.transitions.append(nfa.Transition(EPSILON, st1.id))
    fn1.transitions.append(nfa.Transition(EPSILON, end.id))

    return start, end



# Creacion de automata de un solo simbolo
# Regresa los 2 estados creados, cada uno con sus transiciones
def single(tree, automata):
    symbol = tree.data
    first = nfa.State(len(automata.states))
    automata.states.append(first)
    second = nfa.State(len(automata.states))
    automata.states.append(second)
    first.transitions.append(nfa.Transition(symbol, second.id))
    return first, second


def printE():
    print(EPSILON)
