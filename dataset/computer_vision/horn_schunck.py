
from typing import SupportsIndex

import numpy as np
from scipy.ndimage import convolve


def warp(
    image: np.ndarray, horizontal_flow: np.ndarray, vertical_flow: np.ndarray
) -> np.ndarray:
    
    flow = np.stack((horizontal_flow, vertical_flow), 2)

    grid = np.stack(
        np.meshgrid(np.arange(0, image.shape[1]), np.arange(0, image.shape[0])), 2
    )
    grid = np.round(grid - flow).astype(np.int32)

    
    invalid = (grid < 0) | (grid >= np.array([image.shape[1], image.shape[0]]))
    grid[invalid] = 0

    warped = image[grid[:, :, 1], grid[:, :, 0]]

    
    warped[invalid[:, :, 0] | invalid[:, :, 1]] = 0

    return warped


def horn_schunck(
    image0: np.ndarray,
    image1: np.ndarray,
    num_iter: SupportsIndex,
    alpha: float | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    
    if alpha is None:
        alpha = 0.1

    horizontal_flow = np.zeros_like(image0)
    vertical_flow = np.zeros_like(image0)

    kernel_x = np.array([[-1, 1], [-1, 1]]) * 0.25
    kernel_y = np.array([[-1, -1], [1, 1]]) * 0.25
    kernel_t = np.array([[1, 1], [1, 1]]) * 0.25
    kernel_laplacian = np.array(
        [[1 / 12, 1 / 6, 1 / 12], [1 / 6, 0, 1 / 6], [1 / 12, 1 / 6, 1 / 12]]
    )

    
    for _ in range(num_iter):
        warped_image = warp(image0, horizontal_flow, vertical_flow)
        derivative_x = convolve(warped_image, kernel_x) + convolve(image1, kernel_x)
        derivative_y = convolve(warped_image, kernel_y) + convolve(image1, kernel_y)
        derivative_t = convolve(warped_image, kernel_t) + convolve(image1, -kernel_t)

        avg_horizontal_velocity = convolve(horizontal_flow, kernel_laplacian)
        avg_vertical_velocity = convolve(vertical_flow, kernel_laplacian)

        
        update = (
            derivative_x * avg_horizontal_velocity
            + derivative_y * avg_vertical_velocity
            + derivative_t
        )
        update = update / (alpha**2 + derivative_x**2 + derivative_y**2)

        horizontal_flow = avg_horizontal_velocity - derivative_x * update
        vertical_flow = avg_vertical_velocity - derivative_y * update

    return horizontal_flow, vertical_flow


if __name__ == "__main__":
    import doctest

    doctest.testmod()
