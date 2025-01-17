
from __future__ import annotations

import math

import numpy as np
from numpy.linalg import norm


def euclidean(input_a: np.ndarray, input_b: np.ndarray) -> float:
    return math.sqrt(sum(pow(a - b, 2) for a, b in zip(input_a, input_b)))


def similarity_search(
    dataset: np.ndarray, value_array: np.ndarray
) -> list[list[list[float] | float]]:

    if dataset.ndim != value_array.ndim:
        msg = (
            "Wrong input data's dimensions... "
            f"dataset : {dataset.ndim}, value_array : {value_array.ndim}"
        )
        raise ValueError(msg)

    try:
        if dataset.shape[1] != value_array.shape[1]:
            msg = (
                "Wrong input data's shape... "
                f"dataset : {dataset.shape[1]}, value_array : {value_array.shape[1]}"
            )
            raise ValueError(msg)
    except IndexError:
        if dataset.ndim != value_array.ndim:
            raise TypeError("Wrong shape")

    if dataset.dtype != value_array.dtype:
        msg = (
            "Input data have different datatype... "
            f"dataset : {dataset.dtype}, value_array : {value_array.dtype}"
        )
        raise TypeError(msg)

    answer = []

    for value in value_array:
        dist = euclidean(value, dataset[0])
        vector = dataset[0].tolist()

        for dataset_value in dataset[1:]:
            temp_dist = euclidean(value, dataset_value)

            if dist > temp_dist:
                dist = temp_dist
                vector = dataset_value.tolist()

        answer.append([vector, dist])

    return answer


def cosine_similarity(input_a: np.ndarray, input_b: np.ndarray) -> float:
    return float(np.dot(input_a, input_b) / (norm(input_a) * norm(input_b)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
