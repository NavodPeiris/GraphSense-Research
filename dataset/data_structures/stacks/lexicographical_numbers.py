from collections.abc import Iterator


def lexical_order(max_number: int) -> Iterator[int]:

    stack = [1]

    while stack:
        num = stack.pop()
        if num > max_number:
            continue

        yield num
        if (num % 10) != 9:
            stack.append(num + 1)

        stack.append(num * 10)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"Numbers from 1 to 25 in lexical order: {list(lexical_order(26))}")
