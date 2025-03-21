from pathlib import Path

import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_rotation(
    img: np.ndarray, pt1: np.ndarray, pt2: np.ndarray, rows: int, cols: int
) -> np.ndarray:
    matrix = cv2.getAffineTransform(pt1, pt2)
    return cv2.warpAffine(img, matrix, (rows, cols))


if __name__ == "__main__":
    
    image = cv2.imread(
        str(Path(__file__).resolve().parent.parent / "image_data" / "lena.jpg")
    )
    
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    img_rows, img_cols = gray_img.shape

    
    pts1 = np.array([[50, 50], [200, 50], [50, 200]], np.float32)
    pts2 = np.array([[10, 100], [200, 50], [100, 250]], np.float32)
    pts3 = np.array([[50, 50], [150, 50], [120, 200]], np.float32)
    pts4 = np.array([[10, 100], [80, 50], [180, 250]], np.float32)

    
    images = [
        gray_img,
        get_rotation(gray_img, pts1, pts2, img_rows, img_cols),
        get_rotation(gray_img, pts2, pts3, img_rows, img_cols),
        get_rotation(gray_img, pts2, pts4, img_rows, img_cols),
    ]

    
    fig = plt.figure(1)
    titles = ["Original", "Rotation 1", "Rotation 2", "Rotation 3"]
    for i, image in enumerate(images):
        plt.subplot(2, 2, i + 1), plt.imshow(image, "gray")
        plt.title(titles[i])
        plt.axis("off")
        plt.subplots_adjust(left=0.0, bottom=0.05, right=1.0, top=0.95)
    plt.show()
