
from __future__ import annotations

from collections.abc import Generator


def collatz_sequence(n: int) -> Generator[int]:
    if not isinstance(n, int) or n < 1:
        raise Exception("Sequence only defined for positive integers")

    yield n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n


def main():
    n = int(input("Your number: "))
    sequence = tuple(collatz_sequence(n))
    print(sequence)
    print(f"Collatz sequence from {n} took {len(sequence)} steps.")


if __name__ == "__main__":
    main()
