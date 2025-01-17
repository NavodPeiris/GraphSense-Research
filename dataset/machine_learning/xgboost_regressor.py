
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


def data_handling(data: dict) -> tuple:
    
    return (data["data"], data["target"])


def xgboost(
    features: np.ndarray, target: np.ndarray, test_features: np.ndarray
) -> np.ndarray:
    xgb = XGBRegressor(
        verbosity=0, random_state=42, tree_method="exact", base_score=0.5
    )
    xgb.fit(features, target)
    
    predictions = xgb.predict(test_features)
    predictions = predictions.reshape(len(predictions), 1)
    return predictions


def main() -> None:
    
    california = fetch_california_housing()
    data, target = data_handling(california)
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.25, random_state=1
    )
    predictions = xgboost(x_train, y_train, x_test)
    
    print(f"Mean Absolute Error: {mean_absolute_error(y_test, predictions)}")
    print(f"Mean Square Error: {mean_squared_error(y_test, predictions)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
