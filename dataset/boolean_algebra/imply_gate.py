


def imply_gate(input_1: int, input_2: int) -> int:
    
    return int(input_1 == 0 or input_2 == 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
