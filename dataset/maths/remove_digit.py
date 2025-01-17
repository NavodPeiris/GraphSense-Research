def remove_digit(num: int) -> int:

    if not isinstance(num, int):
        raise TypeError("only integers accepted as input")
    else:
        num_str = str(abs(num))
        num_transpositions = [list(num_str) for char in range(len(num_str))]
        for index in range(len(num_str)):
            num_transpositions[index].pop(index)
        return max(
            int("".join(list(transposition))) for transposition in num_transpositions
        )


if __name__ == "__main__":
    __import__("doctest").testmod()
