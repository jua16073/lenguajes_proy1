import trees as t

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
UNITARY = ['*', '+', '?']

# r* = r+ | e
# r? = r | e
# r+ = r*r

def print_tree(tree):
    print(tree.data)
    if tree.left != None:
        print_tree(tree.left)
    if tree.right != None:
        print_tree(tree.right)

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
            tree = t.Tree()
            tree.data = val
            values.append(tree)
            i -= 1

        elif exp[i] == ")":
            while len(ops) != 0 and ops[-1] != "(":
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                tree = t.Tree()
                tree.data = op
                tree.left = val1
                tree.right = val2
                values.append(tree)
            ops.pop()
        
        else:
            if (exp[i] in UNITARY):
                op = exp[i]
                val = values.pop()
                tree = t.Tree()
                tree.data = op
                tree.left = val
                tree.right = None
                values.append(tree)
            else:
                while (len(ops) != 0  and ops[-1] != '('):
                    op = ops.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    tree = t.Tree()
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
        tree = t.Tree()
        tree.data = op
        tree.left = val1
        tree.right = val2
        values.append(tree)
        if (len(values) == 1):
            return values[-1]
    return values[-1]


if __name__ == "__main__":
    '''
    print("ingrese expression regular: \n")
    exp = input()
    print("ingrese cadena")
    cad = input()'''
    ans = evaluate("a.(a.b)+")
    t.print2DUtil(ans, 5)
