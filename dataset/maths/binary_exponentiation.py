

def binary_exp_recursive(base: float, exponent: int) -> float:
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")

    if exponent == 0:
        return 1

    if exponent % 2 == 1:
        return binary_exp_recursive(base, exponent - 1) * base

    b = binary_exp_recursive(base, exponent // 2)
    return b * b


def binary_exp_iterative(base: float, exponent: int) -> float:
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")

    res: int | float = 1
    while exponent > 0:
        if exponent & 1:
            res *= base

        base *= base
        exponent >>= 1

    return res


def binary_exp_mod_recursive(base: float, exponent: int, modulus: int) -> float:
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer")

    if exponent == 0:
        return 1

    if exponent % 2 == 1:
        return (binary_exp_mod_recursive(base, exponent - 1, modulus) * base) % modulus

    r = binary_exp_mod_recursive(base, exponent // 2, modulus)
    return (r * r) % modulus


def binary_exp_mod_iterative(base: float, exponent: int, modulus: int) -> float:
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer")

    res: int | float = 1
    while exponent > 0:
        if exponent & 1:
            res = ((res % modulus) * (base % modulus)) % modulus

        base *= base
        exponent >>= 1

    return res


if __name__ == "__main__":
    from timeit import timeit

    a = 1269380576
    b = 374
    c = 34

    runs = 100_000
    print(
        timeit(
            f"binary_exp_recursive({a}, {b})",
            setup="from __main__ import binary_exp_recursive",
            number=runs,
        )
    )
    print(
        timeit(
            f"binary_exp_iterative({a}, {b})",
            setup="from __main__ import binary_exp_iterative",
            number=runs,
        )
    )
    print(
        timeit(
            f"binary_exp_mod_recursive({a}, {b}, {c})",
            setup="from __main__ import binary_exp_mod_recursive",
            number=runs,
        )
    )
    print(
        timeit(
            f"binary_exp_mod_iterative({a}, {b}, {c})",
            setup="from __main__ import binary_exp_mod_iterative",
            number=runs,
        )
    )
