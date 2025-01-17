

def run_length_encode(text: str) -> list:
    
    encoded = []
    count = 1

    for i in range(len(text)):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
        else:
            encoded.append((text[i], count))
            count = 1

    return encoded


def run_length_decode(encoded: list) -> str:
    
    return "".join(char * length for char, length in encoded)


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="run_length_encode", verbose=True)
    testmod(name="run_length_decode", verbose=True)
