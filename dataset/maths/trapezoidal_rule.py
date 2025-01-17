

def trapezoidal_rule(boundary, steps):
    h = (boundary[1] - boundary[0]) / steps
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    y = 0.0
    y += (h / 2.0) * f(a)
    for i in x_i:
        y += h * f(i)
    y += (h / 2.0) * f(b)
    return y


def make_points(a, b, h):
    x = a + h
    while x <= (b - h):
        yield x
        x += h


def f(x):
    return x**2


def main():
    a = 0.0
    b = 1.0
    steps = 10.0
    boundary = [a, b]
    y = trapezoidal_rule(boundary, steps)
    print(f"y = {y}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
