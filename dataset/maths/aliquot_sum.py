def aliquot_sum(input_num: int) -> int:
    if not isinstance(input_num, int):
        raise ValueError("Input must be an integer")
    if input_num <= 0:
        raise ValueError("Input must be positive")
    return sum(
        divisor for divisor in range(1, input_num // 2 + 1) if input_num % divisor == 0
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
