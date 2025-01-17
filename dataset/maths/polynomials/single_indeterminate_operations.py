
from __future__ import annotations

from collections.abc import MutableSequence


class Polynomial:
    def __init__(self, degree: int, coefficients: MutableSequence[float]) -> None:
        if len(coefficients) != degree + 1:
            raise ValueError(
                "The number of coefficients should be equal to the degree + 1."
            )

        self.coefficients: list[float] = list(coefficients)
        self.degree = degree

    def __add__(self, polynomial_2: Polynomial) -> Polynomial:

        if self.degree > polynomial_2.degree:
            coefficients = self.coefficients[:]
            for i in range(polynomial_2.degree + 1):
                coefficients[i] += polynomial_2.coefficients[i]
            return Polynomial(self.degree, coefficients)
        else:
            coefficients = polynomial_2.coefficients[:]
            for i in range(self.degree + 1):
                coefficients[i] += self.coefficients[i]
            return Polynomial(polynomial_2.degree, coefficients)

    def __sub__(self, polynomial_2: Polynomial) -> Polynomial:
        return self + polynomial_2 * Polynomial(0, [-1])

    def __neg__(self) -> Polynomial:
        return Polynomial(self.degree, [-c for c in self.coefficients])

    def __mul__(self, polynomial_2: Polynomial) -> Polynomial:
        coefficients: list[float] = [0] * (self.degree + polynomial_2.degree + 1)
        for i in range(self.degree + 1):
            for j in range(polynomial_2.degree + 1):
                coefficients[i + j] += (
                    self.coefficients[i] * polynomial_2.coefficients[j]
                )

        return Polynomial(self.degree + polynomial_2.degree, coefficients)

    def evaluate(self, substitution: float) -> float:
        result: int | float = 0
        for i in range(self.degree + 1):
            result += self.coefficients[i] * (substitution**i)
        return result

    def __str__(self) -> str:
        polynomial = ""
        for i in range(self.degree, -1, -1):
            if self.coefficients[i] == 0:
                continue
            elif self.coefficients[i] > 0:
                if polynomial:
                    polynomial += " + "
            else:
                polynomial += " - "

            if i == 0:
                polynomial += str(abs(self.coefficients[i]))
            elif i == 1:
                polynomial += str(abs(self.coefficients[i])) + "x"
            else:
                polynomial += str(abs(self.coefficients[i])) + "x^" + str(i)

        return polynomial

    def __repr__(self) -> str:
        return self.__str__()

    def derivative(self) -> Polynomial:
        coefficients: list[float] = [0] * self.degree
        for i in range(self.degree):
            coefficients[i] = self.coefficients[i + 1] * (i + 1)
        return Polynomial(self.degree - 1, coefficients)

    def integral(self, constant: float = 0) -> Polynomial:
        coefficients: list[float] = [0] * (self.degree + 2)
        coefficients[0] = constant
        for i in range(self.degree + 1):
            coefficients[i + 1] = self.coefficients[i] / (i + 1)
        return Polynomial(self.degree + 1, coefficients)

    def __eq__(self, polynomial_2: object) -> bool:
        if not isinstance(polynomial_2, Polynomial):
            return False

        if self.degree != polynomial_2.degree:
            return False

        for i in range(self.degree + 1):
            if self.coefficients[i] != polynomial_2.coefficients[i]:
                return False

        return True

    def __ne__(self, polynomial_2: object) -> bool:
        return not self.__eq__(polynomial_2)
