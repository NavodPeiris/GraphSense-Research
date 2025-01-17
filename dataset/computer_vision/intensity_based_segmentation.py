
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def segment_image(image: np.ndarray, thresholds: list[int]) -> np.ndarray:
    
    segmented = np.zeros_like(image, dtype=np.int32)

    
    for i, threshold in enumerate(thresholds):
        segmented[image > threshold] = i + 1

    return segmented


if __name__ == "__main__":
    
    image_path = "path_to_image"  
    original_image = Image.open(image_path).convert("L")
    image_array = np.array(original_image)

    
    thresholds = [50, 100, 150, 200]

    
    segmented_image = segment_image(image_array, thresholds)

    
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image_array, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Segmented Image")
    plt.imshow(segmented_image, cmap="tab20")
    plt.axis("off")

    plt.show()
