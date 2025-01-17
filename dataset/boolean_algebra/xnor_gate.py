

def xnor_gate(input_1: int, input_2: int) -> int:
    
    return 1 if input_1 == input_2 else 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
