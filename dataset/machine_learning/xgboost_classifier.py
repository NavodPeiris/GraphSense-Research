
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def data_handling(data: dict) -> tuple:
    
    
    return (data["data"], data["target"])


def xgboost(features: np.ndarray, target: np.ndarray) -> XGBClassifier:
    classifier = XGBClassifier()
    classifier.fit(features, target)
    return classifier


def main() -> None:

    
    iris = load_iris()
    features, targets = data_handling(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25
    )

    names = iris["target_names"]

    
    xgboost_classifier = xgboost(x_train, y_train)

    
    ConfusionMatrixDisplay.from_estimator(
        xgboost_classifier,
        x_test,
        y_test,
        display_labels=names,
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
