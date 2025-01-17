










import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets










def sigmoid_function(z: float | np.ndarray) -> float | np.ndarray:
    return 1 / (1 + np.exp(-z))


def cost_function(h: np.ndarray, y: np.ndarray) -> float:
    return float((-y * np.log(h) - (1 - y) * np.log(1 - h)).mean())


def log_likelihood(x, y, weights):
    scores = np.dot(x, weights)
    return np.sum(y * scores - np.log(1 + np.exp(scores)))



def logistic_reg(alpha, x, y, max_iterations=70000):
    theta = np.zeros(x.shape[1])

    for iterations in range(max_iterations):
        z = np.dot(x, theta)
        h = sigmoid_function(z)
        gradient = np.dot(x.T, h - y) / y.size
        theta = theta - alpha * gradient  
        z = np.dot(x, theta)
        h = sigmoid_function(z)
        j = cost_function(h, y)
        if iterations % 100 == 0:
            print(f"loss: {j} \t")  
    return theta




if __name__ == "__main__":
    import doctest

    doctest.testmod()

    iris = datasets.load_iris()
    x = iris.data[:, :2]
    y = (iris.target != 0) * 1

    alpha = 0.1
    theta = logistic_reg(alpha, x, y, max_iterations=70000)
    print("theta: ", theta)  

    def predict_prob(x):
        return sigmoid_function(
            np.dot(x, theta)
        )  

    plt.figure(figsize=(10, 6))
    plt.scatter(x[y == 0][:, 0], x[y == 0][:, 1], color="b", label="0")
    plt.scatter(x[y == 1][:, 0], x[y == 1][:, 1], color="r", label="1")
    (x1_min, x1_max) = (x[:, 0].min(), x[:, 0].max())
    (x2_min, x2_max) = (x[:, 1].min(), x[:, 1].max())
    (xx1, xx2) = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
    grid = np.c_[xx1.ravel(), xx2.ravel()]
    probs = predict_prob(grid).reshape(xx1.shape)
    plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors="black")

    plt.legend()
    plt.show()
