

def prime_sieve_eratosthenes(num: int) -> list[int]:

    if num <= 0:
        raise ValueError("Input must be a positive integer")

    primes = [True] * (num + 1)

    p = 2
    while p * p <= num:
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1

    return [prime for prime in range(2, num + 1) if primes[prime]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_num = int(input("Enter a positive integer: ").strip())
    print(prime_sieve_eratosthenes(user_num))
