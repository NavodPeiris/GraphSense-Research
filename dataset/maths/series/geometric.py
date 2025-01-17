

def is_geometric_series(series: list) -> bool:
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [2, 4, 8]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    if len(series) == 1:
        return True
    try:
        common_ratio = series[1] / series[0]
        for index in range(len(series) - 1):
            if series[index + 1] / series[index] != common_ratio:
                return False
    except ZeroDivisionError:
        return False
    return True


def geometric_mean(series: list) -> float:
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [2, 4, 8]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    answer = 1
    for value in series:
        answer *= value
    return pow(answer, 1 / len(series))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
