import cv2
import numpy as np


def get_neighbors_pixel(
    image: np.ndarray, x_coordinate: int, y_coordinate: int, center: int
) -> int:

    try:
        return int(image[x_coordinate][y_coordinate] >= center)
    except (IndexError, TypeError):
        return 0


def local_binary_value(image: np.ndarray, x_coordinate: int, y_coordinate: int) -> int:
    center = image[x_coordinate][y_coordinate]
    powers = [1, 2, 4, 8, 16, 32, 64, 128]

    
    if center is None:
        return 0

    
    binary_values = [
        get_neighbors_pixel(image, x_coordinate - 1, y_coordinate + 1, center),
        get_neighbors_pixel(image, x_coordinate, y_coordinate + 1, center),
        get_neighbors_pixel(image, x_coordinate - 1, y_coordinate, center),
        get_neighbors_pixel(image, x_coordinate + 1, y_coordinate + 1, center),
        get_neighbors_pixel(image, x_coordinate + 1, y_coordinate, center),
        get_neighbors_pixel(image, x_coordinate + 1, y_coordinate - 1, center),
        get_neighbors_pixel(image, x_coordinate, y_coordinate - 1, center),
        get_neighbors_pixel(image, x_coordinate - 1, y_coordinate - 1, center),
    ]

    
    return sum(
        binary_value * power for binary_value, power in zip(binary_values, powers)
    )


if __name__ == "__main__":
    
    image = cv2.imread(
        "digital_image_processing/image_data/lena.jpg", cv2.IMREAD_GRAYSCALE
    )

    
    lbp_image = np.zeros((image.shape[0], image.shape[1]))

    
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            lbp_image[i][j] = local_binary_value(image, i, j)

    cv2.imshow("local binary pattern", lbp_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
