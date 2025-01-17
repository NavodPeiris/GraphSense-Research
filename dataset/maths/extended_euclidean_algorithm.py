





from __future__ import annotations

import sys


def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int]:
    
    if abs(a) == 1:
        return a, 0
    elif abs(b) == 1:
        return 0, b

    old_remainder, remainder = a, b
    old_coeff_a, coeff_a = 1, 0
    old_coeff_b, coeff_b = 0, 1

    while remainder != 0:
        quotient = old_remainder // remainder
        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_coeff_a, coeff_a = coeff_a, old_coeff_a - quotient * coeff_a
        old_coeff_b, coeff_b = coeff_b, old_coeff_b - quotient * coeff_b

    
    if a < 0:
        old_coeff_a = -old_coeff_a
    if b < 0:
        old_coeff_b = -old_coeff_b

    return old_coeff_a, old_coeff_b


def main():
    if len(sys.argv) < 3:
        print("2 integer arguments required")
        return 1
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(extended_euclidean_algorithm(a, b))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
