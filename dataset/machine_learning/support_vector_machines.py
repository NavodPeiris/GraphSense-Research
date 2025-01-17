import numpy as np
from numpy import ndarray
from scipy.optimize import Bounds, LinearConstraint, minimize


def norm_squared(vector: ndarray) -> float:
    return np.dot(vector, vector)


class SVC:

    def __init__(
        self,
        *,
        regularization: float = np.inf,
        kernel: str = "linear",
        gamma: float = 0.0,
    ) -> None:
        self.regularization = regularization
        self.gamma = gamma
        if kernel == "linear":
            self.kernel = self.__linear
        elif kernel == "rbf":
            if self.gamma == 0:
                raise ValueError("rbf kernel requires gamma")
            if not isinstance(self.gamma, (float, int)):
                raise ValueError("gamma must be float or int")
            if not self.gamma > 0:
                raise ValueError("gamma must be > 0")
            self.kernel = self.__rbf
            
            
            
        else:
            msg = f"Unknown kernel: {kernel}"
            raise ValueError(msg)

    
    def __linear(self, vector1: ndarray, vector2: ndarray) -> float:
        return np.dot(vector1, vector2)

    def __rbf(self, vector1: ndarray, vector2: ndarray) -> float:
        return np.exp(-(self.gamma * norm_squared(vector1 - vector2)))

    def fit(self, observations: list[ndarray], classes: ndarray) -> None:

        self.observations = observations
        self.classes = classes

        
        
        
        
        
        
        
        
        
        
        
        
        
        

        (n,) = np.shape(classes)

        def to_minimize(candidate: ndarray) -> float:
            s = 0
            (n,) = np.shape(candidate)
            for i in range(n):
                for j in range(n):
                    s += (
                        candidate[i]
                        * candidate[j]
                        * classes[i]
                        * classes[j]
                        * self.kernel(observations[i], observations[j])
                    )
            return 1 / 2 * s - sum(candidate)

        ly_contraint = LinearConstraint(classes, 0, 0)
        l_bounds = Bounds(0, self.regularization)

        l_star = minimize(
            to_minimize, np.ones(n), bounds=l_bounds, constraints=[ly_contraint]
        ).x
        self.optimum = l_star

        
        s = 0
        for i in range(n):
            for j in range(n):
                s += classes[i] - classes[i] * self.optimum[i] * self.kernel(
                    observations[i], observations[j]
                )
        self.offset = s / n

    def predict(self, observation: ndarray) -> int:
        s = sum(
            self.optimum[n]
            * self.classes[n]
            * self.kernel(self.observations[n], observation)
            for n in range(len(self.classes))
        )
        return 1 if s + self.offset >= 0 else -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
