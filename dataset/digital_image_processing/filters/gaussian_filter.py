
from itertools import product

from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros


def gen_gaussian_kernel(k_size, sigma):
    center = k_size // 2
    x, y = mgrid[0 - center : k_size - center, 0 - center : k_size - center]
    g = 1 / (2 * pi * sigma) * exp(-(square(x) + square(y)) / (2 * square(sigma)))
    return g


def gaussian_filter(image, k_size, sigma):
    height, width = image.shape[0], image.shape[1]
    
    dst_height = height - k_size + 1
    dst_width = width - k_size + 1

    
    image_array = zeros((dst_height * dst_width, k_size * k_size))
    for row, (i, j) in enumerate(product(range(dst_height), range(dst_width))):
        window = ravel(image[i : i + k_size, j : j + k_size])
        image_array[row, :] = window

    
    gaussian_kernel = gen_gaussian_kernel(k_size, sigma)
    filter_array = ravel(gaussian_kernel)

    
    dst = dot(image_array, filter_array).reshape(dst_height, dst_width).astype(uint8)

    return dst


if __name__ == "__main__":
    
    img = imread(r"../image_data/lena.jpg")
    
    gray = cvtColor(img, COLOR_BGR2GRAY)

    
    gaussian3x3 = gaussian_filter(gray, 3, sigma=1)
    gaussian5x5 = gaussian_filter(gray, 5, sigma=0.8)

    
    imshow("gaussian filter with 3x3 mask", gaussian3x3)
    imshow("gaussian filter with 5x5 mask", gaussian5x5)
    waitKey()
