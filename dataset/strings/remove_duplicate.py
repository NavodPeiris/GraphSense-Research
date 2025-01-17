def remove_duplicates(sentence: str) -> str:
    return " ".join(sorted(set(sentence.split())))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
