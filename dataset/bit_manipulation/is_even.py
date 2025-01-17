def is_even(number: int) -> bool:
    
    return number & 1 == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
