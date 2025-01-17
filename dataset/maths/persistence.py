def multiplicative_persistence(num: int) -> int:

    if not isinstance(num, int):
        raise ValueError("multiplicative_persistence() only accepts integral values")
    if num < 0:
        raise ValueError("multiplicative_persistence() does not accept negative values")

    steps = 0
    num_string = str(num)

    while len(num_string) != 1:
        numbers = [int(i) for i in num_string]

        total = 1
        for i in range(len(numbers)):
            total *= numbers[i]

        num_string = str(total)

        steps += 1
    return steps


def additive_persistence(num: int) -> int:

    if not isinstance(num, int):
        raise ValueError("additive_persistence() only accepts integral values")
    if num < 0:
        raise ValueError("additive_persistence() does not accept negative values")

    steps = 0
    num_string = str(num)

    while len(num_string) != 1:
        numbers = [int(i) for i in num_string]

        total = 0
        for i in range(len(numbers)):
            total += numbers[i]

        num_string = str(total)

        steps += 1
    return steps


if __name__ == "__main__":
    import doctest

    doctest.testmod()
