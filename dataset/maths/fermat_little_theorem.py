






def binary_exponentiation(a: int, n: float, mod: int) -> int:
    if n == 0:
        return 1

    elif n % 2 == 1:
        return (binary_exponentiation(a, n - 1, mod) * a) % mod

    else:
        b = binary_exponentiation(a, n / 2, mod)
        return (b * b) % mod



p = 701

a = 1000000000
b = 10


print((a / b) % p == (a * binary_exponentiation(b, p - 2, p)) % p)


print((a / b) % p == (a * b ** (p - 2)) % p)
