

def add(first: int, second: int) -> int:
    while second != 0:
        c = first & second
        first ^= second
        second = c << 1
    return first


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    first = int(input("Enter the first number: ").strip())
    second = int(input("Enter the second number: ").strip())
    print(f"{add(first, second) = }")
