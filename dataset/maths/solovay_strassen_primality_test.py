
import random


def jacobi_symbol(random_a: int, number: int) -> int:

    if random_a in (0, 1):
        return random_a

    random_a %= number
    t = 1

    while random_a != 0:
        while random_a % 2 == 0:
            random_a //= 2
            r = number % 8
            if r in (3, 5):
                t = -t

        random_a, number = number, random_a

        if random_a % 4 == number % 4 == 3:
            t = -t

        random_a %= number

    return t if number == 1 else 0


def solovay_strassen(number: int, iterations: int) -> bool:

    if number <= 1:
        return False
    if number <= 3:
        return True

    for _ in range(iterations):
        a = random.randint(2, number - 2)
        x = jacobi_symbol(a, number)
        y = pow(a, (number - 1) // 2, number)

        if x == 0 or y != x % number:
            return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
