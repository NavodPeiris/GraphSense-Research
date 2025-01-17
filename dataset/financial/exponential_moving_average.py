
from collections.abc import Iterator


def exponential_moving_average(
    stock_prices: Iterator[float], window_size: int
) -> Iterator[float]:

    if window_size <= 0:
        raise ValueError("window_size must be > 0")

    
    alpha = 2 / (1 + window_size)

    
    moving_average = 0.0

    for i, stock_price in enumerate(stock_prices):
        if i <= window_size:
            
            
            moving_average = (moving_average + stock_price) * 0.5 if i else stock_price
        else:
            
            
            moving_average = (alpha * stock_price) + ((1 - alpha) * moving_average)
        yield moving_average


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    stock_prices = [2.0, 5, 3, 8.2, 6, 9, 10]
    window_size = 3
    result = tuple(exponential_moving_average(iter(stock_prices), window_size))
    print(f"{stock_prices = }")
    print(f"{window_size = }")
    print(f"{result = }")
