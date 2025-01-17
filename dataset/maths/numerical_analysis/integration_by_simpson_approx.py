


N_STEPS = 1000


def f(x: float) -> float:
    return x * x




def simpson_integration(function, a: float, b: float, precision: int = 4) -> float:
    assert callable(function), (
        f"the function(object) passed should be callable your input : {function}"
    )
    assert isinstance(a, (float, int)), f"a should be float or integer your input : {a}"
    assert isinstance(function(a), (float, int)), (
        "the function should return integer or float return type of your function, "
        f"{type(a)}"
    )
    assert isinstance(b, (float, int)), f"b should be float or integer your input : {b}"
    assert isinstance(precision, int) and precision > 0, (
        f"precision should be positive integer your input : {precision}"
    )

    
    

    h = (b - a) / N_STEPS
    result = function(a) + function(b)

    for i in range(1, N_STEPS):
        a1 = a + h * i
        result += function(a1) * (4 if i % 2 else 2)

    result *= h / 3
    return round(result, precision)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
