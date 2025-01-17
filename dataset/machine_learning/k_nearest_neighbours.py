
from collections import Counter
from heapq import nsmallest

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


class KNN:
    def __init__(
        self,
        train_data: np.ndarray[float],
        train_target: np.ndarray[int],
        class_labels: list[str],
    ) -> None:
        self.data = zip(train_data, train_target)
        self.labels = class_labels

    @staticmethod
    def _euclidean_distance(a: np.ndarray[float], b: np.ndarray[float]) -> float:
        return float(np.linalg.norm(a - b))

    def classify(self, pred_point: np.ndarray[float], k: int = 5) -> str:
        
        distances = (
            (self._euclidean_distance(data_point[0], pred_point), data_point[1])
            for data_point in self.data
        )

        
        votes = (i[1] for i in nsmallest(k, distances))

        
        result = Counter(votes).most_common(1)[0][0]
        return self.labels[result]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    iris = datasets.load_iris()

    X = np.array(iris["data"])
    y = np.array(iris["target"])
    iris_classes = iris["target_names"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    iris_point = np.array([4.4, 3.1, 1.3, 1.4])
    classifier = KNN(X_train, y_train, iris_classes)
    print(classifier.classify(iris_point, k=3))
