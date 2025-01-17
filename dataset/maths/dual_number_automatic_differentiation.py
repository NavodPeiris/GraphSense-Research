from math import factorial



class Dual:
    def __init__(self, real, rank):
        self.real = real
        if isinstance(rank, int):
            self.duals = [1] * rank
        else:
            self.duals = rank

    def __repr__(self):
        s = "+".join(f"{dual}E{n}" for n, dual in enumerate(self.duals, 1))
        return f"{self.real}+{s}"

    def reduce(self):
        cur = self.duals.copy()
        while cur[-1] == 0:
            cur.pop(-1)
        return Dual(self.real, cur)

    def __add__(self, other):
        if not isinstance(other, Dual):
            return Dual(self.real + other, self.duals)
        s_dual = self.duals.copy()
        o_dual = other.duals.copy()
        if len(s_dual) > len(o_dual):
            o_dual.extend([1] * (len(s_dual) - len(o_dual)))
        elif len(s_dual) < len(o_dual):
            s_dual.extend([1] * (len(o_dual) - len(s_dual)))
        new_duals = []
        for i in range(len(s_dual)):
            new_duals.append(s_dual[i] + o_dual[i])
        return Dual(self.real + other.real, new_duals)

    __radd__ = __add__

    def __sub__(self, other):
        return self + other * -1

    def __mul__(self, other):
        if not isinstance(other, Dual):
            new_duals = []
            for i in self.duals:
                new_duals.append(i * other)
            return Dual(self.real * other, new_duals)
        new_duals = [0] * (len(self.duals) + len(other.duals) + 1)
        for i, item in enumerate(self.duals):
            for j, jtem in enumerate(other.duals):
                new_duals[i + j + 1] += item * jtem
        for k in range(len(self.duals)):
            new_duals[k] += self.duals[k] * other.real
        for index in range(len(other.duals)):
            new_duals[index] += other.duals[index] * self.real
        return Dual(self.real * other.real, new_duals)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, Dual):
            new_duals = []
            for i in self.duals:
                new_duals.append(i / other)
            return Dual(self.real / other, new_duals)
        raise ValueError

    def __floordiv__(self, other):
        if not isinstance(other, Dual):
            new_duals = []
            for i in self.duals:
                new_duals.append(i // other)
            return Dual(self.real // other, new_duals)
        raise ValueError

    def __pow__(self, n):
        if n < 0 or isinstance(n, float):
            raise ValueError("power must be a positive integer")
        if n == 0:
            return 1
        if n == 1:
            return self
        x = self
        for _ in range(n - 1):
            x *= self
        return x


def differentiate(func, position, order):
    if not callable(func):
        raise ValueError("differentiate() requires a function as input for func")
    if not isinstance(position, (float, int)):
        raise ValueError("differentiate() requires a float as input for position")
    if not isinstance(order, int):
        raise ValueError("differentiate() requires an int as input for order")
    d = Dual(position, 1)
    result = func(d)
    if order == 0:
        return result.real
    return result.duals[order - 1] * factorial(order)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    def f(y):
        return y**2 * y**4

    print(differentiate(f, 9, 2))
