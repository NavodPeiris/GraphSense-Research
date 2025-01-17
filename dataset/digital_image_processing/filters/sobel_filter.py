


import numpy as np
from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey

from digital_image_processing.filters.convolve import img_convolve


def sobel_filter(image):
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    dst_x = np.abs(img_convolve(image, kernel_x))
    dst_y = np.abs(img_convolve(image, kernel_y))
    
    dst_x = dst_x * 255 / np.max(dst_x)
    dst_y = dst_y * 255 / np.max(dst_y)

    dst_xy = np.sqrt((np.square(dst_x)) + (np.square(dst_y)))
    dst_xy = dst_xy * 255 / np.max(dst_xy)
    dst = dst_xy.astype(np.uint8)

    theta = np.arctan2(dst_y, dst_x)
    return dst, theta


if __name__ == "__main__":
    
    img = imread("../image_data/lena.jpg")
    
    gray = cvtColor(img, COLOR_BGR2GRAY)

    sobel_grad, sobel_theta = sobel_filter(gray)

    
    imshow("sobel filter", sobel_grad)
    imshow("sobel theta", sobel_theta)
    waitKey(0)
