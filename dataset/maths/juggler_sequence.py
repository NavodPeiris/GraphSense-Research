

import math


def juggler_sequence(number: int) -> list[int]:
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 1:
        msg = f"Input value of [number={number}] must be a positive integer"
        raise ValueError(msg)
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number = math.floor(math.sqrt(number))
        else:
            number = math.floor(
                math.sqrt(number) * math.sqrt(number) * math.sqrt(number)
            )
        sequence.append(number)
    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
