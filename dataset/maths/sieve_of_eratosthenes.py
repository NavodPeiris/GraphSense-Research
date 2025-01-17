
from __future__ import annotations

import math


def prime_sieve(num: int) -> list[int]:

    if num <= 0:
        msg = f"{num}: Invalid input, please enter a positive integer."
        raise ValueError(msg)

    sieve = [True] * (num + 1)
    prime = []
    start = 2
    end = int(math.sqrt(num))

    while start <= end:
        
        if sieve[start] is True:
            prime.append(start)

            
            for i in range(start * start, num + 1, start):
                if sieve[i] is True:
                    sieve[i] = False

        start += 1

    for j in range(end + 1, num + 1):
        if sieve[j] is True:
            prime.append(j)

    return prime


if __name__ == "__main__":
    print(prime_sieve(int(input("Enter a positive integer: ").strip())))
