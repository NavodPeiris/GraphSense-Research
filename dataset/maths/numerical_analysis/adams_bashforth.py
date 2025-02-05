
from collections.abc import Callable
from dataclasses import dataclass

import numpy as np


@dataclass
class AdamsBashforth:

    func: Callable[[float, float], float]
    x_initials: list[float]
    y_initials: list[float]
    step_size: float
    x_final: float

    def __post_init__(self) -> None:
        if self.x_initials[-1] >= self.x_final:
            raise ValueError(
                "The final value of x must be greater than the initial values of x."
            )

        if self.step_size <= 0:
            raise ValueError("Step size must be positive.")

        if not all(
            round(x1 - x0, 10) == self.step_size
            for x0, x1 in zip(self.x_initials, self.x_initials[1:])
        ):
            raise ValueError("x-values must be equally spaced according to step size.")

    def step_2(self) -> np.ndarray:

        if len(self.x_initials) != 2 or len(self.y_initials) != 2:
            raise ValueError("Insufficient initial points information.")

        x_0, x_1 = self.x_initials[:2]
        y_0, y_1 = self.y_initials[:2]

        n = int((self.x_final - x_1) / self.step_size)
        y = np.zeros(n + 2)
        y[0] = y_0
        y[1] = y_1

        for i in range(n):
            y[i + 2] = y[i + 1] + (self.step_size / 2) * (
                3 * self.func(x_1, y[i + 1]) - self.func(x_0, y[i])
            )
            x_0 = x_1
            x_1 += self.step_size

        return y

    def step_3(self) -> np.ndarray:
        if len(self.x_initials) != 3 or len(self.y_initials) != 3:
            raise ValueError("Insufficient initial points information.")

        x_0, x_1, x_2 = self.x_initials[:3]
        y_0, y_1, y_2 = self.y_initials[:3]

        n = int((self.x_final - x_2) / self.step_size)
        y = np.zeros(n + 4)
        y[0] = y_0
        y[1] = y_1
        y[2] = y_2

        for i in range(n + 1):
            y[i + 3] = y[i + 2] + (self.step_size / 12) * (
                23 * self.func(x_2, y[i + 2])
                - 16 * self.func(x_1, y[i + 1])
                + 5 * self.func(x_0, y[i])
            )
            x_0 = x_1
            x_1 = x_2
            x_2 += self.step_size

        return y

    def step_4(self) -> np.ndarray:

        if len(self.x_initials) != 4 or len(self.y_initials) != 4:
            raise ValueError("Insufficient initial points information.")

        x_0, x_1, x_2, x_3 = self.x_initials[:4]
        y_0, y_1, y_2, y_3 = self.y_initials[:4]

        n = int((self.x_final - x_3) / self.step_size)
        y = np.zeros(n + 4)
        y[0] = y_0
        y[1] = y_1
        y[2] = y_2
        y[3] = y_3

        for i in range(n):
            y[i + 4] = y[i + 3] + (self.step_size / 24) * (
                55 * self.func(x_3, y[i + 3])
                - 59 * self.func(x_2, y[i + 2])
                + 37 * self.func(x_1, y[i + 1])
                - 9 * self.func(x_0, y[i])
            )
            x_0 = x_1
            x_1 = x_2
            x_2 = x_3
            x_3 += self.step_size

        return y

    def step_5(self) -> np.ndarray:

        if len(self.x_initials) != 5 or len(self.y_initials) != 5:
            raise ValueError("Insufficient initial points information.")

        x_0, x_1, x_2, x_3, x_4 = self.x_initials[:5]
        y_0, y_1, y_2, y_3, y_4 = self.y_initials[:5]

        n = int((self.x_final - x_4) / self.step_size)
        y = np.zeros(n + 6)
        y[0] = y_0
        y[1] = y_1
        y[2] = y_2
        y[3] = y_3
        y[4] = y_4

        for i in range(n + 1):
            y[i + 5] = y[i + 4] + (self.step_size / 720) * (
                1901 * self.func(x_4, y[i + 4])
                - 2774 * self.func(x_3, y[i + 3])
                - 2616 * self.func(x_2, y[i + 2])
                - 1274 * self.func(x_1, y[i + 1])
                + 251 * self.func(x_0, y[i])
            )
            x_0 = x_1
            x_1 = x_2
            x_2 = x_3
            x_3 = x_4
            x_4 += self.step_size

        return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
