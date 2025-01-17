def binomial_coefficient(n: int, r: int) -> int:
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative integers")
    if 0 in (n, r):
        return 1
    c = [0 for i in range(r + 1)]
    
    c[0] = 1
    for i in range(1, n + 1):
        
        j = min(i, r)
        while j > 0:
            c[j] += c[j - 1]
            j -= 1
    return c[r]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(binomial_coefficient(n=10, r=5))
