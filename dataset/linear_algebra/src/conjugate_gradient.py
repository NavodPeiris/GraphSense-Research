
from typing import Any

import numpy as np


def _is_matrix_spd(matrix: np.ndarray) -> bool:
    
    assert np.shape(matrix)[0] == np.shape(matrix)[1]

    
    if np.allclose(matrix, matrix.T) is False:
        return False

    
    eigen_values, _ = np.linalg.eigh(matrix)

    
    
    return bool(np.all(eigen_values > 0))


def _create_spd_matrix(dimension: int) -> Any:
    rng = np.random.default_rng()
    random_matrix = rng.normal(size=(dimension, dimension))
    spd_matrix = np.dot(random_matrix, random_matrix.T)
    assert _is_matrix_spd(spd_matrix)
    return spd_matrix


def conjugate_gradient(
    spd_matrix: np.ndarray,
    load_vector: np.ndarray,
    max_iterations: int = 1000,
    tol: float = 1e-8,
) -> Any:
    
    assert np.shape(spd_matrix)[0] == np.shape(spd_matrix)[1]
    assert np.shape(load_vector)[0] == np.shape(spd_matrix)[0]
    assert _is_matrix_spd(spd_matrix)

    
    x0 = np.zeros((np.shape(load_vector)[0], 1))
    r0 = np.copy(load_vector)
    p0 = np.copy(r0)

    
    error_residual = 1e9
    error_x_solution = 1e9
    error = 1e9

    
    iterations = 0

    while error > tol:
        
        w = np.dot(spd_matrix, p0)

        

        
        alpha = np.dot(r0.T, r0) / np.dot(p0.T, w)
        
        x = x0 + alpha * p0
        
        r = r0 - alpha * w
        
        beta = np.dot(r.T, r) / np.dot(r0.T, r0)
        
        p = r + beta * p0

        
        error_residual = np.linalg.norm(r - r0)
        error_x_solution = np.linalg.norm(x - x0)
        error = np.maximum(error_residual, error_x_solution)

        
        x0 = np.copy(x)
        r0 = np.copy(r)
        p0 = np.copy(p)

        
        iterations += 1
        if iterations > max_iterations:
            break

    return x


def test_conjugate_gradient() -> None:
    
    dimension = 3
    spd_matrix = _create_spd_matrix(dimension)
    rng = np.random.default_rng()
    x_true = rng.normal(size=(dimension, 1))
    b = np.dot(spd_matrix, x_true)

    
    x_numpy = np.linalg.solve(spd_matrix, b)

    
    x_conjugate_gradient = conjugate_gradient(spd_matrix, b)

    
    assert np.linalg.norm(x_numpy - x_true) <= 1e-6
    assert np.linalg.norm(x_conjugate_gradient - x_true) <= 1e-6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_conjugate_gradient()
