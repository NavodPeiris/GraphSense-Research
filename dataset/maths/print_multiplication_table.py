def multiplication_table(number: int, number_of_terms: int) -> str:
    return "\n".join(
        f"{number} * {i} = {number * i}" for i in range(1, number_of_terms + 1)
    )


if __name__ == "__main__":
    print(multiplication_table(number=5, number_of_terms=10))
