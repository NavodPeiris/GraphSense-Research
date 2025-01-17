

def combinations(n: int, k: int) -> int:

    
    
    if n < k or k < 0:
        raise ValueError("Please enter positive integers for n and k where n >= k")
    res = 1
    for i in range(k):
        res *= n - i
        res //= i + 1
    return res


if __name__ == "__main__":
    print(
        "The number of five-card hands possible from a standard",
        f"fifty-two card deck is: {combinations(52, 5)}\n",
    )

    print(
        "If a class of 40 students must be arranged into groups of",
        f"4 for group projects, there are {combinations(40, 4)} ways",
        "to arrange them.\n",
    )

    print(
        "If 10 teams are competing in a Formula One race, there",
        f"are {combinations(10, 3)} ways that first, second and",
        "third place can be awarded.",
    )
