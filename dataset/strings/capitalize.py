from string import ascii_lowercase, ascii_uppercase


def capitalize(sentence: str) -> str:
    if not sentence:
        return ""

    
    
    
    lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
    return lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
