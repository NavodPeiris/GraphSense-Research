

def harmonic_series(n_term: str) -> list:
    if n_term == "":
        return []
    series: list = []
    for temp in range(int(n_term)):
        series.append(f"1/{temp + 1}" if series else "1")
    return series


if __name__ == "__main__":
    nth_term = input("Enter the last number (nth term) of the Harmonic Series")
    print("Formula of Harmonic Series => 1+1/2+1/3 ..... 1/n")
    print(harmonic_series(nth_term))
