

def is_balanced(s: str) -> bool:
    open_to_closed = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for symbol in s:
        if symbol in open_to_closed:
            stack.append(symbol)
        elif symbol in open_to_closed.values() and (
            not stack or open_to_closed[stack.pop()] != symbol
        ):
            return False
    return not stack  


def main():
    s = input("Enter sequence of brackets: ")
    print(f"'{s}' is {'' if is_balanced(s) else 'not '}balanced.")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    main()
