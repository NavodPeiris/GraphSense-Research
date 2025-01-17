from math import log2


def binary_count_trailing_zeros(a: int) -> int:
    
    if a < 0:
        raise ValueError("Input value must be a positive integer")
    elif isinstance(a, float):
        raise TypeError("Input value must be a 'int' type")
    return 0 if (a == 0) else int(log2(a & -a))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
