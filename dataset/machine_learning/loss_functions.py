import numpy as np


def binary_cross_entropy(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  
    bce_loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return np.mean(bce_loss)


def binary_focal_cross_entropy(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    gamma: float = 2.0,
    alpha: float = 0.25,
    epsilon: float = 1e-15,
) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")
    
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    bcfe_loss = -(
        alpha * (1 - y_pred) ** gamma * y_true * np.log(y_pred)
        + (1 - alpha) * y_pred**gamma * (1 - y_true) * np.log(1 - y_pred)
    )

    return np.mean(bcfe_loss)


def categorical_cross_entropy(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    if y_true.shape != y_pred.shape:
        raise ValueError("Input arrays must have the same shape.")

    if np.any((y_true != 0) & (y_true != 1)) or np.any(y_true.sum(axis=1) != 1):
        raise ValueError("y_true must be one-hot encoded.")

    if not np.all(np.isclose(np.sum(y_pred, axis=1), 1, rtol=epsilon, atol=epsilon)):
        raise ValueError("Predicted probabilities must sum to approximately 1.")

    y_pred = np.clip(y_pred, epsilon, 1)  
    return -np.sum(y_true * np.log(y_pred))


def categorical_focal_cross_entropy(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    alpha: np.ndarray = None,
    gamma: float = 2.0,
    epsilon: float = 1e-15,
) -> float:
    if y_true.shape != y_pred.shape:
        raise ValueError("Shape of y_true and y_pred must be the same.")

    if alpha is None:
        alpha = np.ones(y_true.shape[1])

    if np.any((y_true != 0) & (y_true != 1)) or np.any(y_true.sum(axis=1) != 1):
        raise ValueError("y_true must be one-hot encoded.")

    if len(alpha) != y_true.shape[1]:
        raise ValueError("Length of alpha must match the number of classes.")

    if not np.all(np.isclose(np.sum(y_pred, axis=1), 1, rtol=epsilon, atol=epsilon)):
        raise ValueError("Predicted probabilities must sum to approximately 1.")

    
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    
    cfce_loss = -np.sum(
        alpha * np.power(1 - y_pred, gamma) * y_true * np.log(y_pred), axis=1
    )

    return np.mean(cfce_loss)


def hinge_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Length of predicted and actual array must be same.")

    if np.any((y_true != -1) & (y_true != 1)):
        raise ValueError("y_true can have values -1 or 1 only.")

    hinge_losses = np.maximum(0, 1.0 - (y_true * y_pred))
    return np.mean(hinge_losses)


def huber_loss(y_true: np.ndarray, y_pred: np.ndarray, delta: float) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    huber_mse = 0.5 * (y_true - y_pred) ** 2
    huber_mae = delta * (np.abs(y_true - y_pred) - 0.5 * delta)
    return np.where(np.abs(y_true - y_pred) <= delta, huber_mse, huber_mae).mean()


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    squared_errors = (y_true - y_pred) ** 2
    return np.mean(squared_errors)


def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    return np.mean(abs(y_true - y_pred))


def mean_squared_logarithmic_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    squared_logarithmic_errors = (np.log1p(y_true) - np.log1p(y_pred)) ** 2
    return np.mean(squared_logarithmic_errors)


def mean_absolute_percentage_error(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("The length of the two arrays should be the same.")

    y_true = np.where(y_true == 0, epsilon, y_true)
    absolute_percentage_diff = np.abs((y_true - y_pred) / y_true)

    return np.mean(absolute_percentage_diff)


def perplexity_loss(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-7
) -> float:

    vocab_size = y_pred.shape[2]

    if y_true.shape[0] != y_pred.shape[0]:
        raise ValueError("Batch size of y_true and y_pred must be equal.")
    if y_true.shape[1] != y_pred.shape[1]:
        raise ValueError("Sentence length of y_true and y_pred must be equal.")
    if np.max(y_true) > vocab_size:
        raise ValueError("Label value must not be greater than vocabulary size.")

    
    filter_matrix = np.array(
        [[list(np.eye(vocab_size)[word]) for word in sentence] for sentence in y_true]
    )

    
    true_class_pred = np.sum(y_pred * filter_matrix, axis=2).clip(epsilon, 1)

    
    perp_losses = np.exp(np.negative(np.mean(np.log(true_class_pred), axis=1)))

    return np.mean(perp_losses)


def smooth_l1_loss(y_true: np.ndarray, y_pred: np.ndarray, beta: float = 1.0) -> float:

    if len(y_true) != len(y_pred):
        raise ValueError("The length of the two arrays should be the same.")

    diff = np.abs(y_true - y_pred)
    loss = np.where(diff < beta, 0.5 * diff**2 / beta, diff - 0.5 * beta)
    return np.mean(loss)


def kullback_leibler_divergence(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    kl_loss = y_true * np.log(y_true / y_pred)
    return np.sum(kl_loss)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
