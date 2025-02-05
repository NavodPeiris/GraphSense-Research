


from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import array, dot, pad, ravel, uint8, zeros


def im2col(image, block_size):
    rows, cols = image.shape
    dst_height = cols - block_size[1] + 1
    dst_width = rows - block_size[0] + 1
    image_array = zeros((dst_height * dst_width, block_size[1] * block_size[0]))
    row = 0
    for i in range(dst_height):
        for j in range(dst_width):
            window = ravel(image[i : i + block_size[0], j : j + block_size[1]])
            image_array[row, :] = window
            row += 1

    return image_array


def img_convolve(image, filter_kernel):
    height, width = image.shape[0], image.shape[1]
    k_size = filter_kernel.shape[0]
    pad_size = k_size // 2
    
    image_tmp = pad(image, pad_size, mode="edge")

    
    image_array = im2col(image_tmp, (k_size, k_size))

    
    kernel_array = ravel(filter_kernel)
    
    dst = dot(image_array, kernel_array).reshape(height, width)
    return dst


if __name__ == "__main__":
    
    img = imread(r"../image_data/lena.jpg")
    
    gray = cvtColor(img, COLOR_BGR2GRAY)
    
    Laplace_kernel = array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    out = img_convolve(gray, Laplace_kernel).astype(uint8)
    imshow("Laplacian", out)
    waitKey(0)
