
from __future__ import annotations


def list_of_submasks(mask: int) -> list[int]:

    assert isinstance(mask, int) and mask > 0, (
        f"mask needs to be positive integer, your input {mask}"
    )

    all_submasks = []
    submask = mask

    while submask:
        all_submasks.append(submask)
        submask = (submask - 1) & mask

    return all_submasks


if __name__ == "__main__":
    import doctest

    doctest.testmod()
