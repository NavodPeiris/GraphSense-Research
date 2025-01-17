
from maths.greatest_common_divisor import greatest_common_divisor


def power(x: int, y: int, mod: int) -> int:

    if y == 0:
        return 1
    temp = power(x, y // 2, mod) % mod
    temp = (temp * temp) % mod
    if y % 2 == 1:
        temp = (temp * x) % mod
    return temp


def is_carmichael_number(n: int) -> bool:

    if n <= 0 or not isinstance(n, int):
        msg = f"Number {n} must instead be a positive integer"
        raise ValueError(msg)

    return all(
        power(b, n - 1, n) == 1
        for b in range(2, n)
        if greatest_common_divisor(b, n) == 1
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    number = int(input("Enter number: ").strip())
    if is_carmichael_number(number):
        print(f"{number} is a Carmichael Number.")
    else:
        print(f"{number} is not a Carmichael Number.")
