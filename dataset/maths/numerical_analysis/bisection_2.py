

def equation(x: float) -> float:
    return 10 - x * x


def bisection(a: float, b: float) -> float:
    
    if equation(a) * equation(b) >= 0:
        raise ValueError("Wrong space!")

    c = a
    while (b - a) >= 0.01:
        
        c = (a + b) / 2
        
        if equation(c) == 0.0:
            break
        
        if equation(c) * equation(a) < 0:
            b = c
        else:
            a = c
    return c


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(bisection(-2, 5))
    print(bisection(0, 6))
