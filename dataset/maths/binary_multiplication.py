

def binary_multiply(a: int, b: int) -> int:
    res = 0
    while b > 0:
        if b & 1:
            res += a

        a += a
        b >>= 1

    return res


def binary_mod_multiply(a: int, b: int, modulus: int) -> int:
    res = 0
    while b > 0:
        if b & 1:
            res = ((res % modulus) + (a % modulus)) % modulus

        a += a
        b >>= 1

    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
