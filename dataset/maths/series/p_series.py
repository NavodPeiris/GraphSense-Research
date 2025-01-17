
from __future__ import annotations


def p_series(nth_term: float | str, power: float | str) -> list[str]:
    if nth_term == "":
        return [""]
    nth_term = int(nth_term)
    power = int(power)
    series: list[str] = []
    for temp in range(int(nth_term)):
        series.append(f"1 / {pow(temp + 1, int(power))}" if series else "1")
    return series


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    nth_term = int(input("Enter the last number (nth term) of the P-Series"))
    power = int(input("Enter the power for  P-Series"))
    print("Formula of P-Series => 1+1/2^p+1/3^p ..... 1/n^p")
    print(p_series(nth_term, power))
