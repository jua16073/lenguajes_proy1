# Metodo directo

import nfa as automata
import trees
import dfa_set as dfa
import evaluate as eval
import collections

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
EPSILON = "ε"

def directo(tree, exp):
    new_tree = trees.Tree()
    new_tree.data = "."
    right_t = trees.Tree()
    right_t.data = "#"
    new_tree.right = right_t
    new_tree.left = tree

    # Estados importantes
    importantes = estados_importantes(new_tree)
    # FirstPos
    first = first_pos(new_tree)
    #Lastpos
    last = last_pos(new_tree)
    # Followpos
    table = {}
    for pos in importantes:
        table[pos] = []
    followpos(new_tree, table)

    inicial = first_pos(new_tree)
    final = last_pos(new_tree)
    auto_direct = create(inicial, final, table, exp)
    return auto_direct

def create(inicial, final, table, exp):
    auto_direct = automata.Automata(exp)
    first = automata.State(inicial, len(auto_direct.states))
    auto_direct.states.append(first)
    if final[-1] in first.id:
        first.accept = True
    symbols = []
    for symbol in exp:
        if symbol not in OPERATORS and symbol not in symbols and symbol != EPSILON:
            symbols.append(symbol)
    
    for state in auto_direct.states:
        for symbol in symbols:
            temp = []
            for pos in state.id:
                if pos.data == symbol:
                    tos = table[pos]
                    for t in tos:
                        if t not in temp:
                            temp.append(t)
            if dfa.check(auto_direct, temp) and temp != []:
                new_state = automata.State(temp, len(auto_direct.states))
                if final[-1] in temp:
                    new_state.accept = True
                auto_direct.states.append(new_state)
                state.transitions.append(automata.Transition(symbol, auto_direct.states[-1].id2))
            elif temp != []:
                selected = eval.select(auto_direct, temp)
                if selected:
                    state.transitions.append(automata.Transition(symbol, selected.id2))
                else:
                    print("No existe nodo con ", temp, " de id")
    return auto_direct

def estados_importantes(tree, num = 0):
    nodes = []
    if tree.data not in OPERATORS and tree.data != EPSILON and tree.left == None and tree.right == None:
        nodes.append(tree)
    if tree.left != None:
        resp = estados_importantes(tree.left, num)
        for i in resp:
            nodes.append(i)
    if tree.right != None:
        resp = estados_importantes(tree.right, num)
        for i in resp:
            nodes.append(i)
    return nodes

def nullable(tree):
    if tree.data == EPSILON:
        return True
    elif tree.data == ".":
        if nullable(tree.left) and nullable(tree.right):
            return True
    elif tree.data == "*":
        return True
    elif tree.data == "|":
        if nullable(tree.left) or nullable(tree.right):
            return True
        else:
            return False
    elif tree.data == "+":
        if nullable(tree.left):
            return True
        else:
            return False
    elif tree.data == "?":
        return True
    return False

def first_pos(tree):
    pos = []
    if tree.data in OPERATORS:
        if tree.data == "|":
            temp1 = first_pos(tree.left)
            temp2 = first_pos(tree.right)
            for num in temp1:
                pos.append(num)
            for num in temp2:
                pos.append(num)
        elif tree.data == "*":
            temp1 = first_pos(tree.left)
            for num in temp1:
                pos.append(num)
        elif tree.data == ".":
            temp1 = first_pos(tree.left)
            for num in temp1:
                pos.append(num)
            if nullable(tree.left):
                temp2 = first_pos(tree.right)
                for num in temp2:
                    pos.append(num)
        elif tree.data == "+":
            temp1 = first_pos(tree.left)
            for num in temp1:
                pos.append(num)
        elif tree.data == "?":
            temp1 = first_pos(tree.left)
            for num in temp1:
                pos.append(num)
    elif tree.data != EPSILON:
        pos.append(tree)
    return pos

def last_pos(tree):
    pos = []
    if tree.data in OPERATORS:
        if tree.data == "|":
            temp1 = last_pos(tree.left)
            temp2 = last_pos(tree.right)
            for num in temp1:
                pos.append(num)
            for num in temp2:
                pos.append(num)
        elif tree.data == "*":
            temp1 = last_pos(tree.left)
            for num in temp1:
                pos.append(num)
        elif tree.data == ".":
            temp1 = last_pos(tree.right)
            if nullable(tree.right):
                temp2 = last_pos(tree.left)
                for num in temp2:
                    pos.append(num)
            for num in temp1:
                pos.append(num)
        elif tree.data == "+":
            temp1 = last_pos(tree.left)
            for num in temp1:
                pos.append(num)
        elif tree.data == "?":
            temp1 = last_pos(tree.left)
            for num in temp1:
                pos.append(num)
    elif tree.data != EPSILON:
        pos.append(tree)
    return pos

def followpos(tree, table):
    if tree.data == ".":
        temp1 = last_pos(tree.left)
        temp2 = first_pos(tree.right)
        for i in temp1:
            for num in temp2:
                table[i].append(num)
    elif tree.data == "*":
        temp1 = last_pos(tree)
        temp2 = first_pos(tree)
        for i in temp1:
            for num in temp2:
                table[i].append(num)
    elif tree.data == "+":
        temp1 = last_pos(tree.left)
        temp2 = first_pos(tree.left)
        for i in temp1:
            for num in temp2:
                table[i].append(num)

    if tree.left != None:
        followpos(tree.left, table)
    if tree.right != None:
        followpos(tree.right, table)
