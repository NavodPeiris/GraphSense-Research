
calc = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def is_operand(c):
    return c.isdigit()


def evaluate(expression):
    stack = []

    
    for c in expression.split()[::-1]:
        
        if is_operand(c):
            stack.append(int(c))

        else:
            
            
            o1 = stack.pop()
            o2 = stack.pop()
            stack.append(calc[c](o1, o2))

    return stack.pop()



if __name__ == "__main__":
    test_expression = "+ 9 * 2 6"
    print(evaluate(test_expression))

    test_expression = "/ * 10 2 + 4 1 "
    print(evaluate(test_expression))
