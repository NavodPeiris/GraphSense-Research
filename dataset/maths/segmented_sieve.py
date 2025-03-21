
import math


def sieve(n: int) -> list[int]:

    if n <= 0 or isinstance(n, float):
        msg = f"Number {n} must instead be a positive integer"
        raise ValueError(msg)

    in_prime = []
    start = 2
    end = int(math.sqrt(n))  
    temp = [True] * (end + 1)
    prime = []

    while start <= end:
        if temp[start] is True:
            in_prime.append(start)
            for i in range(start * start, end + 1, start):
                temp[i] = False
        start += 1
    prime += in_prime

    low = end + 1
    high = min(2 * end, n)

    while low <= n:
        temp = [True] * (high - low + 1)
        for each in in_prime:
            t = math.floor(low / each) * each
            if t < low:
                t += each

            for j in range(t, high + 1, each):
                temp[j - low] = False

        for j in range(len(temp)):
            if temp[j] is True:
                prime.append(j + low)

        low = high + 1
        high = min(high + end, n)

    return prime


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{sieve(10**6) = }")
