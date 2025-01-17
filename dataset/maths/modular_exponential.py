


def modular_exponential(base: int, power: int, mod: int):

    if power < 0:
        return -1
    base %= mod
    result = 1

    while power > 0:
        if power & 1:
            result = (result * base) % mod
        power = power >> 1
        base = (base * base) % mod

    return result


def main():
    print(modular_exponential(3, 200, 13))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
