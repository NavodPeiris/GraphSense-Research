

import numpy as np
from cv2 import COLOR_BGR2GRAY, CV_8UC3, cvtColor, filter2D, imread, imshow, waitKey


def gabor_filter_kernel(
    ksize: int, sigma: int, theta: int, lambd: int, gamma: int, psi: int
) -> np.ndarray:

    
    
    if (ksize % 2) == 0:
        ksize = ksize + 1
    gabor = np.zeros((ksize, ksize), dtype=np.float32)

    
    for y in range(ksize):
        for x in range(ksize):
            
            px = x - ksize // 2
            py = y - ksize // 2

            
            _theta = theta / 180 * np.pi
            cos_theta = np.cos(_theta)
            sin_theta = np.sin(_theta)

            
            _x = cos_theta * px + sin_theta * py

            
            _y = -sin_theta * px + cos_theta * py

            
            gabor[y, x] = np.exp(-(_x**2 + gamma**2 * _y**2) / (2 * sigma**2)) * np.cos(
                2 * np.pi * _x / lambd + psi
            )

    return gabor


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
    img = imread("../image_data/lena.jpg")
    
    gray = cvtColor(img, COLOR_BGR2GRAY)

    
    out = np.zeros(gray.shape[:2])
    for theta in [0, 30, 60, 90, 120, 150]:
        kernel_10 = gabor_filter_kernel(10, 8, theta, 10, 0, 0)
        out += filter2D(gray, CV_8UC3, kernel_10)
    out = out / out.max() * 255
    out = out.astype(np.uint8)

    imshow("Original", gray)
    imshow("Gabor filter with 20x20 mask and 6 directions", out)

    waitKey(0)
