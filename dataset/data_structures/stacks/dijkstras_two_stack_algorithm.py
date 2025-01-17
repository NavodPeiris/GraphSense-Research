
__author__ = "Alexander Joslin"

import operator as op

from .stack import Stack


def dijkstras_two_stack_algorithm(equation: str) -> int:
    operators = {"*": op.mul, "/": op.truediv, "+": op.add, "-": op.sub}

    operand_stack: Stack[int] = Stack()
    operator_stack: Stack[str] = Stack()

    for i in equation:
        if i.isdigit():
            
            operand_stack.push(int(i))
        elif i in operators:
            
            operator_stack.push(i)
        elif i == ")":
            
            opr = operator_stack.peek()
            operator_stack.pop()
            num1 = operand_stack.peek()
            operand_stack.pop()
            num2 = operand_stack.peek()
            operand_stack.pop()

            total = operators[opr](num2, num1)
            operand_stack.push(total)

    
    return operand_stack.peek()


if __name__ == "__main__":
    equation = "(5 + ((4 * 2) * (2 + 3)))"
    
    print(f"{equation} = {dijkstras_two_stack_algorithm(equation)}")
