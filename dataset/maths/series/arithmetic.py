

def is_arithmetic_series(series: list) -> bool:
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [2, 4, 6]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    if len(series) == 1:
        return True
    common_diff = series[1] - series[0]
    for index in range(len(series) - 1):
        if series[index + 1] - series[index] != common_diff:
            return False
    return True


def arithmetic_mean(series: list) -> float:
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [2, 4, 6]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    answer = 0
    for val in series:
        answer += val
    return answer / len(series)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
