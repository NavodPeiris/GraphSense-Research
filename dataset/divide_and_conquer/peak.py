
from __future__ import annotations


def peak(lst: list[int]) -> int:
    
    m = len(lst) // 2

    
    three = lst[m - 1 : m + 2]

    
    if three[1] > three[0] and three[1] > three[2]:
        return three[1]

    
    elif three[0] < three[2]:
        if len(lst[:m]) == 2:
            m -= 1
        return peak(lst[m:])

    
    else:
        if len(lst[:m]) == 2:
            m += 1
        return peak(lst[:m])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
