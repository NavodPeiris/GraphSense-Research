from pathlib import Path

import numpy as np
from PIL import Image


def rgb_to_gray(rgb: np.ndarray) -> np.ndarray:
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    return 0.2989 * r + 0.5870 * g + 0.1140 * b


def gray_to_binary(gray: np.ndarray) -> np.ndarray:
    return (gray > 127) & (gray <= 255)


def erosion(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    output = np.zeros_like(image)
    image_padded = np.zeros(
        (image.shape[0] + kernel.shape[0] - 1, image.shape[1] + kernel.shape[1] - 1)
    )

    
    image_padded[kernel.shape[0] - 2 : -1 :, kernel.shape[1] - 2 : -1 :] = image

    
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            summation = (
                kernel * image_padded[y : y + kernel.shape[0], x : x + kernel.shape[1]]
            ).sum()
            output[y, x] = int(summation == 5)
    return output


if __name__ == "__main__":
    
    lena_path = Path(__file__).resolve().parent / "image_data" / "lena.jpg"
    lena = np.array(Image.open(lena_path))

    
    structuring_element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])

    
    output = erosion(gray_to_binary(rgb_to_gray(lena)), structuring_element)

    
    pil_img = Image.fromarray(output).convert("RGB")
    pil_img.save("result_erosion.png")
