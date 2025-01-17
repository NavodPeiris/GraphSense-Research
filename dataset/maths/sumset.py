

def sumset(set_a: set, set_b: set) -> set:
    assert isinstance(set_a, set), f"The input value of [set_a={set_a}] is not a set"
    assert isinstance(set_b, set), f"The input value of [set_b={set_b}] is not a set"

    return {a + b for a in set_a for b in set_b}


if __name__ == "__main__":
    from doctest import testmod

    testmod()
