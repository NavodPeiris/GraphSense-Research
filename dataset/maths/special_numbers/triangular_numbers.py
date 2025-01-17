

def triangular_number(position: int) -> int:
    if position < 0:
        raise ValueError("param `position` must be non-negative")

    return position * (position + 1) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
