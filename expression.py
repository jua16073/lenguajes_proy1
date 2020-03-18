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
    else:
        #exp = "a.(a.b)+"
        #exp = "(a|b)+"
        #exp = "b*.a.b"
        #exp = "(a*|b*).c"
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
        #exp = "(b|b)*.a.b.b.(a|b)*"
        #exp = "(a|b)*.a.b.b"
        #exp = "(a|b)+"
        exp = "b*"
    # Creacion de arbol
    ans = trees.evaluate(exp)

    # Creacion de automatas
    auto = nfa.create_automata(ans, exp)
    graph.graph(auto, "nfa")
    graph.to_txt(auto, "nfa")
    print("////////////////////////\nA dfa")
    auto_dfa = dfa.to_dfa(auto, exp)
    graph.graph(auto_dfa, "dfa_set")
    graph.to_txt(auto, "dfa_set")
    print("////////////////////////\nDirecto")
    auto_direct = directo.directo(ans, exp)
    graph.graph(auto_direct, "dfa_direct")
    graph.to_txt(auto, "dfa_direct")

    # Evaluacion de cadena de caracteres
    while True:
        print("Ingrese expresion a probar")
        prueba = input()

        print("Evaluacion nfa")
        print(eval.is_in_language(auto, prueba))
        print("////////////////////////\nEvaluacion dfa")
        print(eval.is_in_language(auto_dfa, prueba))
        print("////////////////////////\nEvaluacion Directo")
        print(eval.is_in_language(auto_direct, prueba))

        print("evaluar otra? \n s/n")
        prueba = input()
        if prueba  == "n":
            break

    