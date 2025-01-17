


def xor_gate(input_1: int, input_2: int) -> int:
    
    return (input_1, input_2).count(0) % 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
