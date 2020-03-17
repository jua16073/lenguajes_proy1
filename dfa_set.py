# archivo para pasar de un nfa a un dfa
import evaluate as eval
import nfa
import collections

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
EPSILON = "ε"

def to_dfa(automata, regex):
    dfa = nfa.Automata(automata.id)
    print(dfa.id)
    actual = [0]

    # simbolos del lenguaje
    symbols = []
    for symbol in regex:
        if symbol not in OPERATORS and symbol not in symbols and symbol != EPSILON:
            symbols.append(symbol)

    # Metodo de conjuntos
    dfa.states.append(nfa.State(eval.cerradura(automata, actual), len(dfa.states)))
    for state in dfa.states:
        # Busqueda de los movimientos con los simbolos del lenguaje
        for symbol in symbols:
            c_epsilon = []
            temp = []
            for num in state.id:
                for transition in automata.states[num].transitions:
                    #print("de ", automata.states[num].id, " a ", transition.to, " con ", transition.symbol)
                    if transition.symbol == symbol:
                        temp.append(transition.to)
            # Cerradura epsilon del movimiento de los estados con
            # los simbolos   
            c_epsilon = eval.cerradura(automata, temp)
            if check(dfa, c_epsilon) and c_epsilon != []:
                new_s = nfa.State(c_epsilon, len(dfa.states))
                dfa.states.append(new_s)
                if check_aceptacion(automata, c_epsilon):
                    new_s.accept = True
                state.transitions.append(nfa.Transition(symbol, dfa.states[-1].id2))
            elif c_epsilon != []:
                selected = eval.select(dfa, c_epsilon)
                if selected:
                    state.transitions.append(nfa.Transition(symbol, selected.id2))
                else:
                    print("No existe nodo con ", c_epsilon, " de id")

    return dfa
    
    # print("///////////")
    # for state in dfa.states:
    #     for transition in state.transitions:
    #         print("de ", state.id, " a ", transition.to, " con ", transition.symbol)

            

def check(nfa, new_state):
    for state in nfa.states:
        if collections.Counter(state.id) == collections.Counter(new_state):
            return False
    return True

def check_aceptacion(nfa, new_state):
    for num in new_state:
        if nfa.states[num].accept:
            return True
    return False
                    
            