

def nand_gate(input_1: int, input_2: int) -> int:
    
    return int(not (input_1 and input_2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
