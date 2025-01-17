

def sylvester(number: int) -> int:
    assert isinstance(number, int), f"The input value of [n={number}] is not an integer"

    if number == 1:
        return 2
    elif number < 1:
        msg = f"The input value of [n={number}] has to be > 0"
        raise ValueError(msg)
    else:
        num = sylvester(number - 1)
        lower = num - 1
        upper = num
        return lower * upper + 1


if __name__ == "__main__":
    print(f"The 8th number in Sylvester's sequence: {sylvester(8)}")
