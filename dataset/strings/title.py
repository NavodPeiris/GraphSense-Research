def to_title_case(word: str) -> str:

    if "a" <= word[0] <= "z":
        word = chr(ord(word[0]) - 32) + word[1:]

    for i in range(1, len(word)):
        if "A" <= word[i] <= "Z":
            word = word[:i] + chr(ord(word[i]) + 32) + word[i + 1 :]

    return word


def sentence_to_title_case(input_str: str) -> str:

    return " ".join(to_title_case(word) for word in input_str.split())


if __name__ == "__main__":
    from doctest import testmod

    testmod()
