


import logging

import numpy as np
import pytest
from scipy.linalg import eigh

logging.basicConfig(level=logging.INFO, format="%(message)s")


def column_reshape(input_array: np.ndarray) -> np.ndarray:

    return input_array.reshape((input_array.size, 1))


def covariance_within_classes(
    features: np.ndarray, labels: np.ndarray, classes: int
) -> np.ndarray:

    covariance_sum = np.nan
    for i in range(classes):
        data = features[:, labels == i]
        data_mean = data.mean(1)
        
        centered_data = data - column_reshape(data_mean)
        if i > 0:
            
            covariance_sum += np.dot(centered_data, centered_data.T)
        else:
            
            covariance_sum = np.dot(centered_data, centered_data.T)

    return covariance_sum / features.shape[1]


def covariance_between_classes(
    features: np.ndarray, labels: np.ndarray, classes: int
) -> np.ndarray:

    general_data_mean = features.mean(1)
    covariance_sum = np.nan
    for i in range(classes):
        data = features[:, labels == i]
        device_data = data.shape[1]
        data_mean = data.mean(1)
        if i > 0:
            
            covariance_sum += device_data * np.dot(
                column_reshape(data_mean) - column_reshape(general_data_mean),
                (column_reshape(data_mean) - column_reshape(general_data_mean)).T,
            )
        else:
            
            covariance_sum = device_data * np.dot(
                column_reshape(data_mean) - column_reshape(general_data_mean),
                (column_reshape(data_mean) - column_reshape(general_data_mean)).T,
            )

    return covariance_sum / features.shape[1]


def principal_component_analysis(features: np.ndarray, dimensions: int) -> np.ndarray:

    
    if features.any():
        data_mean = features.mean(1)
        
        centered_data = features - np.reshape(data_mean, (data_mean.size, 1))
        covariance_matrix = np.dot(centered_data, centered_data.T) / features.shape[1]
        _, eigenvectors = np.linalg.eigh(covariance_matrix)
        
        filtered_eigenvectors = eigenvectors[:, ::-1][:, 0:dimensions]
        
        projected_data = np.dot(filtered_eigenvectors.T, features)
        logging.info("Principal Component Analysis computed")

        return projected_data
    else:
        logging.basicConfig(level=logging.ERROR, format="%(message)s", force=True)
        logging.error("Dataset empty")
        raise AssertionError


def linear_discriminant_analysis(
    features: np.ndarray, labels: np.ndarray, classes: int, dimensions: int
) -> np.ndarray:

    
    assert classes > dimensions

    
    if features.any:
        _, eigenvectors = eigh(
            covariance_between_classes(features, labels, classes),
            covariance_within_classes(features, labels, classes),
        )
        filtered_eigenvectors = eigenvectors[:, ::-1][:, :dimensions]
        svd_matrix, _, _ = np.linalg.svd(filtered_eigenvectors)
        filtered_svd_matrix = svd_matrix[:, 0:dimensions]
        projected_data = np.dot(filtered_svd_matrix.T, features)
        logging.info("Linear Discriminant Analysis computed")

        return projected_data
    else:
        logging.basicConfig(level=logging.ERROR, format="%(message)s", force=True)
        logging.error("Dataset empty")
        raise AssertionError


def test_linear_discriminant_analysis() -> None:
    
    features = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]])
    labels = np.array([0, 0, 0, 1, 1])
    classes = 2
    dimensions = 2

    
    with pytest.raises(AssertionError) as error_info:  
        projected_data = linear_discriminant_analysis(
            features, labels, classes, dimensions
        )
        if isinstance(projected_data, np.ndarray):
            raise AssertionError(
                "Did not raise AssertionError for dimensions > classes"
            )
        assert error_info.type is AssertionError


def test_principal_component_analysis() -> None:
    features = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    dimensions = 2
    expected_output = np.array([[6.92820323, 8.66025404, 10.39230485], [3.0, 3.0, 3.0]])

    with pytest.raises(AssertionError) as error_info:  
        output = principal_component_analysis(features, dimensions)
        if not np.allclose(expected_output, output):
            raise AssertionError
        assert error_info.type is AssertionError


if __name__ == "__main__":
    import doctest

    doctest.testmod()
