

def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit: int = 0

    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)

    return max_profit


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(max_profit([7, 1, 5, 3, 6, 4]))
