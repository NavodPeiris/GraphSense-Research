

def different_signs(num1: int, num2: int) -> bool:
    
    return num1 ^ num2 < 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
