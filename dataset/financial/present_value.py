

def present_value(discount_rate: float, cash_flows: list[float]) -> float:
    if discount_rate < 0:
        raise ValueError("Discount rate cannot be negative")
    if not cash_flows:
        raise ValueError("Cash flows list cannot be empty")
    present_value = sum(
        cash_flow / ((1 + discount_rate) ** i) for i, cash_flow in enumerate(cash_flows)
    )
    return round(present_value, ndigits=2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
