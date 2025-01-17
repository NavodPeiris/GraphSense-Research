
from collections.abc import Callable

RealFunc = Callable[[float], float]


def calc_derivative(f: RealFunc, x: float, delta_x: float = 1e-3) -> float:
    return (f(x + delta_x / 2) - f(x - delta_x / 2)) / delta_x


def newton_raphson(
    f: RealFunc,
    x0: float = 0,
    max_iter: int = 100,
    step: float = 1e-6,
    max_error: float = 1e-6,
    log_steps: bool = False,
) -> tuple[float, float, list[float]]:

    def f_derivative(x: float) -> float:
        return calc_derivative(f, x, step)

    a = x0  
    steps = []
    for _ in range(max_iter):
        if log_steps:  
            steps.append(a)

        error = abs(f(a))
        if error < max_error:
            return a, error, steps

        if f_derivative(a) == 0:
            raise ZeroDivisionError("No converging solution found, zero derivative")
        a -= f(a) / f_derivative(a)  
    raise ArithmeticError("No converging solution found, iteration limit reached")


if __name__ == "__main__":
    import doctest
    from math import exp, tanh

    doctest.testmod()

    def func(x: float) -> float:
        return tanh(x) ** 2 - exp(3 * x)

    solution, err, steps = newton_raphson(
        func, x0=10, max_iter=100, step=1e-6, log_steps=True
    )
    print(f"{solution=}, {err=}")
    print("\n".join(str(x) for x in steps))
