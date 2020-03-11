import trees
import nfa
import individuales as m
import sys

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
UNITARY = ['*', '+', '?']
EPSILON = "ε"

# r* = r+ | e
# r? = r | e
# r+ = r*r

# Recorrer la regex
def evaluate(exp):
    print(exp)

    values = []
    ops = []
    
    i = 0

    while i < len(exp):

        if exp[i] == ' ':
            i += 1
            continue

        elif exp[i] == "(":
            ops.append(exp[i])
        
        elif exp[i] not in OPERATORS:
            val = ""

            while (i < len(exp)) and exp[i] not in OPERATORS:
                val = str(val) + exp[i]
                i -= -1
            tree = trees.Tree()
            tree.data = val
            values.append(tree)
            i -= 1

        elif exp[i] == ")":
            while len(ops) != 0 and ops[-1] != "(":
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                tree = trees.Tree()
                tree.data = op
                tree.left = val1
                tree.right = val2
                values.append(tree)
            ops.pop()
        
        else:
            if (exp[i] in UNITARY):
                op = exp[i]
                val = values.pop()
                tree = trees.Tree()
                tree.data = op
                tree.left = val
                tree.right = None
                values.append(tree)
            else:
                while (len(ops) != 0  and ops[-1] != '('):
                    op = ops.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    tree = trees.Tree()
                    tree.data = op
                    tree.left = val1
                    tree.right = val2
                    values.append(tree)
                ops.append(exp[i])
        
        i -= -1
    
    while(len(ops) != 0):
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        tree = trees.Tree()
        tree.data = op
        tree.left = val1
        tree.right = val2
        values.append(tree)
        if (len(values) == 1):
            return values[-1]
    return values[-1]

def create_automata(tree, og):
    auto = nfa.Automata(og)
    trees.print2DUtil(tree, 5)
    symbols = nfa.post_order(tree)
    m.t_handler(tree, auto)
    for state in auto.states:
        print(state.id)
        for t in state.transitions:
            print("with: ",t.symbol ," to: ", t.to)


if __name__ == "__main__":
    '''
    print("ingrese expression regular: \n")
    exp = input()
    print("ingrese cadena")
    cad = input()'''
    #exp = "a.(a.b)+"
    #exp = "b*.a.b"
    #exp = "0.(0|1)*.0"
    exp = "(a|b)*.a.(a|b).(a|b)"
    #exp = "(((a.a)|(b.b)).a).(a|b)"
    ans = evaluate(exp)
    create_automata(ans, exp)