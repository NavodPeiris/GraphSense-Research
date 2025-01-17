
from collections.abc import Sequence


def simple_moving_average(
    data: Sequence[float], window_size: int
) -> list[float | None]:
    if window_size < 1:
        raise ValueError("Window size must be a positive integer")

    sma: list[float | None] = []

    for i in range(len(data)):
        if i < window_size - 1:
            sma.append(None)  
        else:
            window = data[i - window_size + 1 : i + 1]
            sma_value = sum(window) / window_size
            sma.append(sma_value)
    return sma


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    
    data = [10, 12, 15, 13, 14, 16, 18, 17, 19, 21]

    
    window_size = 3

    
    sma_values = simple_moving_average(data, window_size)

    
    print("Simple Moving Average (SMA) Values:")
    for i, value in enumerate(sma_values):
        if value is not None:
            print(f"Day {i + 1}: {value:.2f}")
        else:
            print(f"Day {i + 1}: Not enough data for SMA")
