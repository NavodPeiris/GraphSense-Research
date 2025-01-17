

from __future__ import annotations

import math
import random


def rsafactor(d: int, e: int, n: int) -> list[int]:
    
    k = d * e - 1
    p = 0
    q = 0
    while p == 0:
        g = random.randint(2, n - 1)
        t = k
        while True:
            if t % 2 == 0:
                t = t // 2
                x = (g**t) % n
                y = math.gcd(x - 1, n)
                if x > 1 and y > 1:
                    p = y
                    q = n // y
                    break  
            else:
                break  
    return sorted([p, q])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
