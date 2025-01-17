def reverse_words(input_str: str) -> str:
    return " ".join(input_str.split()[::-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
