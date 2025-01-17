def lower(word: str) -> str:

    
    
    
    return "".join(chr(ord(char) + 32) if "A" <= char <= "Z" else char for char in word)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
