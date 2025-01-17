
import struct


def fast_inverse_sqrt(number: float) -> float:
    if number <= 0:
        raise ValueError("Input must be a positive number.")
    i = struct.unpack(">i", struct.pack(">f", number))[0]
    i = 0x5F3759DF - (i >> 1)
    y = struct.unpack(">f", struct.pack(">i", i))[0]
    return y * (1.5 - 0.5 * number * y * y)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
    from math import sqrt

    for i in range(5, 101, 5):
        print(f"{i:>3}: {(1 / sqrt(i)) - fast_inverse_sqrt(i):.5f}")
