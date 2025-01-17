def show_bits(before: int, after: int) -> str:
    
    return f"{before:>5}: {before:08b}\n{after:>5}: {after:08b}"


def swap_odd_even_bits(num: int) -> int:
    
    
    even_bits = num & 0xAAAAAAAA

    
    odd_bits = num & 0x55555555


    return even_bits >> 1 | odd_bits << 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    for i in (-1, 0, 1, 2, 3, 4, 23, 24):
        print(show_bits(i, swap_odd_even_bits(i)), "\n")
