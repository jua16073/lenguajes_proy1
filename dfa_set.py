# archivo para pasar de un nfa a un dfa
import evaluate as eval

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
def to_dfa(automata, regex):
    actual = [0]
    sets = []

    # simbolos del lenguaje
    symbols = []
    for symbol in regex:
        if symbol not in OPERATORS and symbol not in symbols:
            symbols.append(symbol)

    # Metodo de conjuntos
    sets.append(eval.cerradura(automata, actual))
    for state in sets:
        temp = []
        for num in state:
            for transition in automata.states[num].transitions:
                for s in symbols:
                    pass
            pass
    pass