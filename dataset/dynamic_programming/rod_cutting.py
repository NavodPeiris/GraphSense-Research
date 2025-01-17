

def naive_cut_rod_recursive(n: int, prices: list):

    _enforce_args(n, prices)
    if n == 0:
        return 0
    max_revue = float("-inf")
    for i in range(1, n + 1):
        max_revue = max(
            max_revue, prices[i - 1] + naive_cut_rod_recursive(n - i, prices)
        )

    return max_revue


def top_down_cut_rod(n: int, prices: list):
    _enforce_args(n, prices)
    max_rev = [float("-inf") for _ in range(n + 1)]
    return _top_down_cut_rod_recursive(n, prices, max_rev)


def _top_down_cut_rod_recursive(n: int, prices: list, max_rev: list):
    if max_rev[n] >= 0:
        return max_rev[n]
    elif n == 0:
        return 0
    else:
        max_revenue = float("-inf")
        for i in range(1, n + 1):
            max_revenue = max(
                max_revenue,
                prices[i - 1] + _top_down_cut_rod_recursive(n - i, prices, max_rev),
            )

        max_rev[n] = max_revenue

    return max_rev[n]


def bottom_up_cut_rod(n: int, prices: list):
    _enforce_args(n, prices)

    
    
    max_rev = [float("-inf") for _ in range(n + 1)]
    max_rev[0] = 0

    for i in range(1, n + 1):
        max_revenue_i = max_rev[i]
        for j in range(1, i + 1):
            max_revenue_i = max(max_revenue_i, prices[j - 1] + max_rev[i - j])

        max_rev[i] = max_revenue_i

    return max_rev[n]


def _enforce_args(n: int, prices: list):
    if n < 0:
        msg = f"n must be greater than or equal to 0. Got n = {n}"
        raise ValueError(msg)

    if n > len(prices):
        msg = (
            "Each integral piece of rod must have a corresponding price. "
            f"Got n = {n} but length of prices = {len(prices)}"
        )
        raise ValueError(msg)


def main():
    prices = [6, 10, 12, 15, 20, 23]
    n = len(prices)

    
    
    expected_max_revenue = 36

    max_rev_top_down = top_down_cut_rod(n, prices)
    max_rev_bottom_up = bottom_up_cut_rod(n, prices)
    max_rev_naive = naive_cut_rod_recursive(n, prices)

    assert expected_max_revenue == max_rev_top_down
    assert max_rev_top_down == max_rev_bottom_up
    assert max_rev_bottom_up == max_rev_naive


if __name__ == "__main__":
    main()
