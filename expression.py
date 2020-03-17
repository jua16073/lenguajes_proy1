import trees
import nfa
import individuales as m
import evaluate as eval
import sys
import graph
import directo
import dfa_set as dfa

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
EPSILON = "ε"

# r* = r+ | e
# r? = r | e
# r+ = r*r

if __name__ == "__main__":
    print("1. ya hecha\n2. ingresar")
    opcion = input()
    if opcion == "2":
        print("ingrese expression regular: \n")
        exp = input()
        # print("ingrese cadena")
        # cad = input()
    else:
        #exp = "a.(a.b)+"
        exp = "(a|b)+"
        #exp = "b*.a.b"
        exp = "(a*|b*).c"
        #exp = "(a|"+EPSILON+").b.(a+).c?"
        #exp = "0.(0|1)*.0"
        #exp = "0?.(1|"+EPSILON+")?.0*"
        #exp = "(0.0)*.(1.1)*"
        #exp = "(a.b)|c*"
        #exp = "(0.1)*"
        #exp = "a|b"
        #exp = "((a|b)*)*."+EPSILON+".((a|b)|"+EPSILON+")*"
        #exp = "((a|b)*.((a|(b.b))*."+EPSILON+"))"
        #exp = "(((a.a)|(b.b)).a).(a|b)"
        exp = "(b|b)*.a.b.b.(a|b)*"
        #exp = "(a|b)*.a.b.b"
    ans = trees.evaluate(exp)
    auto = nfa.create_automata(ans, exp)
    # for state in auto.states:
    #     print(state.id)
    #     for t in state.transitions:
    #         print("with: ",t.symbol ," to: ", t.to)
    graph.graph(auto, "nfa")
    print("////////////////////////\nEvaluacion nfa")
    print(eval.is_in_language(auto, "bac"))
    print("////////////////////////\nA dfa")
    auto_dfa = dfa.to_dfa(auto, exp)
    graph.graph(auto_dfa, "dfa_set")
    print("////////////////////////\nEvaluacion dfa")
    print(eval.is_in_language(auto_dfa, "c"))
    print("////////////////////////\nDirecto")
    auto_direct = directo.directo(ans, exp)
    graph.graph(auto_direct, "dfa_direct")


    