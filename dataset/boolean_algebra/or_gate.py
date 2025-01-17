


def or_gate(input_1: int, input_2: int) -> int:
    
    return int((input_1, input_2).count(1) != 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
