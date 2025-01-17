
import math


def proth(number: int) -> int:

    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)

    if number < 1:
        msg = f"Input value of [number={number}] must be > 0"
        raise ValueError(msg)
    elif number == 1:
        return 3
    elif number == 2:
        return 5
    else:
        block_index = int(math.log(number // 3, 2)) + 2

        proth_list = [3, 5]
        proth_index = 2
        increment = 3
        for block in range(1, block_index):
            for _ in range(increment):
                proth_list.append(2 ** (block + 1) + proth_list[proth_index - 1])
                proth_index += 1
            increment *= 2

    return proth_list[number - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    for number in range(11):
        value = 0
        try:
            value = proth(number)
        except ValueError:
            print(f"ValueError: there is no {number}th Proth number")
            continue

        print(f"The {number}th Proth number: {value}")
