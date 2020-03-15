# Para graficar 
from graphviz import Digraph


def graph(automata, nombre):
    dot = Digraph(name = "Automata")
    dot.attr(rankdir = "LR")
    for state in automata.states:
        if state.accept:
            dot.node(str(state.id2), str(state.id2), shape = "doublecircle")
        else:
            dot.node(str(state.id2), str(state.id2))
        for transition in state.transitions:
            dot.edge(str(state.id2),str(transition.to), transition.symbol)
    print(dot.source)
    dot.render('test-output/' + nombre + '.gv', view=False)
