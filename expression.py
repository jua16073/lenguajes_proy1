import trees
import nfa
import individuales as m
import evaluate as eval
import sys
import graph
import dfa_set as dfa

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
    start , finish = m.t_handler(tree, auto)
    finish.accept = True
    return auto
    


if __name__ == "__main__":
    '''
    print("ingrese expression regular: \n")
    exp = input()
    print("ingrese cadena")
    cad = input()'''
    exp = "a.(a.b)+"
    #exp = "b*.a.b"
    #exp = "0.(0|1)*.0"
    #exp = "(a.b)|c*"
    #exp = "(0.1)*"
    #exp = "((a|b)*)*."+EPSILON+".((a|b)|"+EPSILON+")*"
    #exp = "((a|b)*.((a|(b.b))*."+EPSILON+"))"
    #exp = "(((a.a)|(b.b)).a).(a|b)"
    #exp = "(b|b)*.a.b.b.(a|b)*"
    ans = evaluate(exp)
    auto = create_automata(ans, exp)
    # for state in auto.states:
    #     print(state.id)
    #     for t in state.transitions:
    #         print("with: ",t.symbol ," to: ", t.to)
    graph.graph(auto)
    print("////////////////////////\nEvaluacion nfa")
    print(eval.is_in_language(auto, "aab"))
    print("////////////////////////\nA dfa")
    dfa.to_dfa(auto, exp)


    