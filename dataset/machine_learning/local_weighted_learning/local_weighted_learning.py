
import matplotlib.pyplot as plt
import numpy as np


def weight_matrix(point: np.ndarray, x_train: np.ndarray, tau: float) -> np.ndarray:
    m = len(x_train)  
    weights = np.eye(m)  
    for j in range(m):
        diff = point - x_train[j]
        weights[j, j] = np.exp(diff @ diff.T / (-2.0 * tau**2))

    return weights


def local_weight(
    point: np.ndarray, x_train: np.ndarray, y_train: np.ndarray, tau: float
) -> np.ndarray:
    weight_mat = weight_matrix(point, x_train, tau)
    weight = np.linalg.inv(x_train.T @ weight_mat @ x_train) @ (
        x_train.T @ weight_mat @ y_train.T
    )

    return weight


def local_weight_regression(
    x_train: np.ndarray, y_train: np.ndarray, tau: float
) -> np.ndarray:
    y_pred = np.zeros(len(x_train))  
    for i, item in enumerate(x_train):
        y_pred[i] = np.dot(item, local_weight(item, x_train, y_train, tau)).item()

    return y_pred


def load_data(
    dataset_name: str, x_name: str, y_name: str
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    import seaborn as sns

    data = sns.load_dataset(dataset_name)
    x_data = np.array(data[x_name])
    y_data = np.array(data[y_name])

    one = np.ones(len(y_data))

    
    x_train = np.column_stack((one, x_data))

    return x_train, x_data, y_data


def plot_preds(
    x_train: np.ndarray,
    preds: np.ndarray,
    x_data: np.ndarray,
    y_data: np.ndarray,
    x_name: str,
    y_name: str,
) -> None:
    x_train_sorted = np.sort(x_train, axis=0)
    plt.scatter(x_data, y_data, color="blue")
    plt.plot(
        x_train_sorted[:, 1],
        preds[x_train[:, 1].argsort(0)],
        color="yellow",
        linewidth=5,
    )
    plt.title("Local Weighted Regression")
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    
    training_data_x, total_bill, tip = load_data("tips", "total_bill", "tip")
    predictions = local_weight_regression(training_data_x, tip, 5)
    plot_preds(training_data_x, predictions, total_bill, tip, "total_bill", "tip")
