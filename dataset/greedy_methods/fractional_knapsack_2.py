



from __future__ import annotations


def fractional_knapsack(
    value: list[int], weight: list[int], capacity: int
) -> tuple[float, list[float]]:
    index = list(range(len(value)))
    ratio = [v / w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value: float = 0
    fractions: list[float] = [0] * len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break

    return max_value, fractions


if __name__ == "__main__":
    import doctest

    doctest.testmod()
