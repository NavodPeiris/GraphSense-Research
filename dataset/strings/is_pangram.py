

def is_pangram(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    
    frequency = set()

    
    input_str = input_str.replace(" ", "")
    for alpha in input_str:
        if "a" <= alpha.lower() <= "z":
            frequency.add(alpha.lower())
    return len(frequency) == 26


def is_pangram_faster(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    flag = [False] * 26
    for char in input_str:
        if char.islower():
            flag[ord(char) - 97] = True
        elif char.isupper():
            flag[ord(char) - 65] = True
    return all(flag)


def is_pangram_fastest(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    return len({char for char in input_str.lower() if char.isalpha()}) == 26


def benchmark() -> None:
    from timeit import timeit

    setup = "from __main__ import is_pangram, is_pangram_faster, is_pangram_fastest"
    print(timeit("is_pangram()", setup=setup))
    print(timeit("is_pangram_faster()", setup=setup))
    print(timeit("is_pangram_fastest()", setup=setup))
    
    


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
