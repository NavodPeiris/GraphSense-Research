

from __future__ import annotations

from scipy.special import comb


class BezierCurve:

    def __init__(self, list_of_points: list[tuple[float, float]]):
        self.list_of_points = list_of_points
        
        
        self.degree = len(list_of_points) - 1

    def basis_function(self, t: float) -> list[float]:
        assert 0 <= t <= 1, "Time t must be between 0 and 1."
        output_values: list[float] = []
        for i in range(len(self.list_of_points)):
            
            output_values.append(
                comb(self.degree, i) * ((1 - t) ** (self.degree - i)) * (t**i)
            )
        
        assert round(sum(output_values), 5) == 1
        return output_values

    def bezier_curve_function(self, t: float) -> tuple[float, float]:

        assert 0 <= t <= 1, "Time t must be between 0 and 1."

        basis_function = self.basis_function(t)
        x = 0.0
        y = 0.0
        for i in range(len(self.list_of_points)):
            
            x += basis_function[i] * self.list_of_points[i][0]
            y += basis_function[i] * self.list_of_points[i][1]
        return (x, y)

    def plot_curve(self, step_size: float = 0.01):
        from matplotlib import pyplot as plt

        to_plot_x: list[float] = []  
        to_plot_y: list[float] = []  

        t = 0.0
        while t <= 1:
            value = self.bezier_curve_function(t)
            to_plot_x.append(value[0])
            to_plot_y.append(value[1])
            t += step_size

        x = [i[0] for i in self.list_of_points]
        y = [i[1] for i in self.list_of_points]

        plt.plot(
            to_plot_x,
            to_plot_y,
            color="blue",
            label="Curve of Degree " + str(self.degree),
        )
        plt.scatter(x, y, color="red", label="Control Points")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    BezierCurve([(1, 2), (3, 5)]).plot_curve()  
    BezierCurve([(0, 0), (5, 5), (5, 0)]).plot_curve()  
    BezierCurve([(0, 0), (5, 5), (5, 0), (2.5, -2.5)]).plot_curve()
