

def median(matrix: list[list[int]]) -> int:
    
    linear = sorted(num for row in matrix for num in row)

    
    mid = (len(linear) - 1) // 2

    
    return linear[mid]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
