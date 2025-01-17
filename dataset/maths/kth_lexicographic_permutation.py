def kth_permutation(k, n):
    
    factorials = [1]
    for i in range(2, n):
        factorials.append(factorials[-1] * i)
    assert 0 <= k < factorials[-1] * n, "k out of bounds"

    permutation = []
    elements = list(range(n))

    
    while factorials:
        factorial = factorials.pop()
        number, k = divmod(k, factorial)
        permutation.append(elements[number])
        elements.remove(elements[number])
    permutation.append(elements[0])

    return permutation


if __name__ == "__main__":
    import doctest

    doctest.testmod()
