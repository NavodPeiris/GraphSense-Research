

def nimply_gate(input_1: int, input_2: int) -> int:
   
    return int(input_1 == 1 and input_2 == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
