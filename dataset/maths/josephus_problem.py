

def josephus_recursive(num_people: int, step_size: int) -> int:
    if (
        not isinstance(num_people, int)
        or not isinstance(step_size, int)
        or num_people <= 0
        or step_size <= 0
    ):
        raise ValueError("num_people or step_size is not a positive integer.")

    if num_people == 1:
        return 0

    return (josephus_recursive(num_people - 1, step_size) + step_size) % num_people


def find_winner(num_people: int, step_size: int) -> int:
    return josephus_recursive(num_people, step_size) + 1


def josephus_iterative(num_people: int, step_size: int) -> int:
    circle = list(range(1, num_people + 1))
    current = 0

    while len(circle) > 1:
        current = (current + step_size - 1) % len(circle)
        circle.pop(current)

    return circle[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
