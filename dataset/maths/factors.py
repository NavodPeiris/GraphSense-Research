from doctest import testmod
from math import sqrt


def factors_of_a_number(num: int) -> list:
    facs: list[int] = []
    if num < 1:
        return facs
    facs.append(1)
    if num == 1:
        return facs
    facs.append(num)
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:  
            facs.append(i)
            d = num // i  
            if d != i:  
                facs.append(d)  
    facs.sort()
    return facs


if __name__ == "__main__":
    testmod(name="factors_of_a_number", verbose=True)
