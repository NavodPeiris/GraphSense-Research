import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


class GradientBoostingClassifier:
    def __init__(self, n_estimators: int = 100, learning_rate: float = 0.1) -> None:
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.models: list[tuple[DecisionTreeRegressor, float]] = []

    def fit(self, features: np.ndarray, target: np.ndarray) -> None:
        for _ in range(self.n_estimators):
            
            residuals = -self.gradient(target, self.predict(features))
            
            model = DecisionTreeRegressor(max_depth=1)
            model.fit(features, residuals)
            
            self.models.append((model, self.learning_rate))

    def predict(self, features: np.ndarray) -> np.ndarray:
        
        predictions = np.zeros(features.shape[0])
        for model, learning_rate in self.models:
            predictions += learning_rate * model.predict(features)
        return np.sign(predictions)  

    def gradient(self, target: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        return -target / (1 + np.exp(target * y_pred))


if __name__ == "__main__":
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
