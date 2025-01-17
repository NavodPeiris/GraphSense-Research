
import matplotlib.pyplot as plt
import numpy as np


class PolynomialRegression:
    __slots__ = "degree", "params"

    def __init__(self, degree: int) -> None:
        if degree < 0:
            raise ValueError("Polynomial degree must be non-negative")

        self.degree = degree
        self.params = None

    @staticmethod
    def _design_matrix(data: np.ndarray, degree: int) -> np.ndarray:
        rows, *remaining = data.shape
        if remaining:
            raise ValueError("Data must have dimensions N x 1")

        return np.vander(data, N=degree + 1, increasing=True)

    def fit(self, x_train: np.ndarray, y_train: np.ndarray) -> None:
        X = PolynomialRegression._design_matrix(x_train, self.degree)  
        _, cols = X.shape
        if np.linalg.matrix_rank(X) < cols:
            raise ArithmeticError(
                "Design matrix is not full rank, can't compute coefficients"
            )

        
        self.params = np.linalg.pinv(X) @ y_train

    def predict(self, data: np.ndarray) -> np.ndarray:
        if self.params is None:
            raise ArithmeticError("Predictor hasn't been fit yet")

        return PolynomialRegression._design_matrix(data, self.degree) @ self.params


def main() -> None:
    import seaborn as sns

    mpg_data = sns.load_dataset("mpg")

    poly_reg = PolynomialRegression(degree=2)
    poly_reg.fit(mpg_data.weight, mpg_data.mpg)

    weight_sorted = np.sort(mpg_data.weight)
    predictions = poly_reg.predict(weight_sorted)

    plt.scatter(mpg_data.weight, mpg_data.mpg, color="gray", alpha=0.5)
    plt.plot(weight_sorted, predictions, color="red", linewidth=3)
    plt.title("Predicting Fuel Efficiency Using Polynomial Regression")
    plt.xlabel("Weight (lbs)")
    plt.ylabel("Fuel Efficiency (mpg)")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
