
from typing import Literal

from .balanced_parentheses import balanced_parentheses
from .stack import Stack

PRECEDENCES: dict[str, int] = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
}
ASSOCIATIVITIES: dict[str, Literal["LR", "RL"]] = {
    "+": "LR",
    "-": "LR",
    "*": "LR",
    "/": "LR",
    "^": "RL",
}


def precedence(char: str) -> int:
    return PRECEDENCES.get(char, -1)


def associativity(char: str) -> Literal["LR", "RL"]:
    return ASSOCIATIVITIES[char]


def infix_to_postfix(expression_str: str) -> str:
    if not balanced_parentheses(expression_str):
        raise ValueError("Mismatched parentheses")
    stack: Stack[str] = Stack()
    postfix = []
    for char in expression_str:
        if char.isalpha() or char.isdigit():
            postfix.append(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            while not stack.is_empty() and stack.peek() != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while True:
                if stack.is_empty():
                    stack.push(char)
                    break

                char_precedence = precedence(char)
                tos_precedence = precedence(stack.peek())

                if char_precedence > tos_precedence:
                    stack.push(char)
                    break
                if char_precedence < tos_precedence:
                    postfix.append(stack.pop())
                    continue
                
                if associativity(char) == "RL":
                    stack.push(char)
                    break
                postfix.append(stack.pop())

    while not stack.is_empty():
        postfix.append(stack.pop())
    return " ".join(postfix)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    expression = "a+b*(c^d-e)^(f+g*h)-i"

    print("Infix to Postfix Notation demonstration:\n")
    print("Infix notation: " + expression)
    print("Postfix notation: " + infix_to_postfix(expression))
