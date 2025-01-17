def count_vowels(s: str) -> int:
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
