def split(string: str, separator: str = " ") -> list:

    split_words = []

    last_index = 0
    for index, char in enumerate(string):
        if char == separator:
            split_words.append(string[last_index:index])
            last_index = index + 1
        if index + 1 == len(string):
            split_words.append(string[last_index : index + 1])
    return split_words


if __name__ == "__main__":
    from doctest import testmod

    testmod()
