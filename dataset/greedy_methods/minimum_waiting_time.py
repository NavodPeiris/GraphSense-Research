

def minimum_waiting_time(queries: list[int]) -> int:
    n = len(queries)
    if n in (0, 1):
        return 0
    return sum(query * (n - i - 1) for i, query in enumerate(sorted(queries)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
