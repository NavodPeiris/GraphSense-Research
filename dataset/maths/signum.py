

def signum(num: float) -> int:
    if num < 0:
        return -1
    return 1 if num else 0


def test_signum() -> None:
    assert signum(5) == 1
    assert signum(-5) == -1
    assert signum(0) == 0
    assert signum(10.5) == 1
    assert signum(-10.5) == -1
    assert signum(1e-6) == 1
    assert signum(-1e-6) == -1
    assert signum(123456789) == 1
    assert signum(-123456789) == -1


if __name__ == "__main__":
    print(signum(12))
    print(signum(-12))
    print(signum(0))
