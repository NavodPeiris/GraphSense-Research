

def create_ngram(sentence: str, ngram_size: int) -> list[str]:
    return [sentence[i : i + ngram_size] for i in range(len(sentence) - ngram_size + 1)]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
