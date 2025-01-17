def upper(word: str) -> str:
    return "".join(chr(ord(char) - 32) if "a" <= char <= "z" else char for char in word)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
