# Archivo para evaluar una expresion
# En un automata

EPSILON = "ε"

def is_in_language(automata, expresion):
    actual = [0]
    actual = cerradura(automata, actual)
    i = 0
    while True:
        temp = []
        for num in actual:
            for transition in automata.states[num].transitions:
                if transition.symbol == expresion[i]:
                    temp.append(transition.to)
        i += 1
        actual = cerradura(automata, temp)
        if not actual:
            break
    print(temp)
    

def cerradura(automata, actual):
    for num in actual:
        for transition in automata.states[num].transitions:
            if transition.symbol == EPSILON:
                actual.append(transition.to)
    print("return actual ", actual)
    return actual