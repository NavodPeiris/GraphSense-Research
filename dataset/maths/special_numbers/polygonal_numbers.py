def polygonal_num(num: int, sides: int) -> int:
    if num < 0 or sides < 3:
        raise ValueError("Invalid input: num must be >= 0 and sides must be >= 3.")

    return ((sides - 2) * num**2 - (sides - 4) * num) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
