
import numpy as np
from cv2 import destroyAllWindows, imread, imshow, waitKey


class Burkes:

    def __init__(self, input_img, threshold: int):
        self.min_threshold = 0
        
        self.max_threshold = int(self.get_greyscale(255, 255, 255))

        if not self.min_threshold < threshold < self.max_threshold:
            msg = f"Factor value should be from 0 to {self.max_threshold}"
            raise ValueError(msg)

        self.input_img = input_img
        self.threshold = threshold
        self.width, self.height = self.input_img.shape[1], self.input_img.shape[0]

        
        
        self.error_table = [
            [0 for _ in range(self.height + 4)] for __ in range(self.width + 1)
        ]
        self.output_img = np.ones((self.width, self.height, 3), np.uint8) * 255

    @classmethod
    def get_greyscale(cls, blue: int, green: int, red: int) -> float:
        return 0.114 * blue + 0.587 * green + 0.299 * red

    def process(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                greyscale = int(self.get_greyscale(*self.input_img[y][x]))
                if self.threshold > greyscale + self.error_table[y][x]:
                    self.output_img[y][x] = (0, 0, 0)
                    current_error = greyscale + self.error_table[y][x]
                else:
                    self.output_img[y][x] = (255, 255, 255)
                    current_error = greyscale + self.error_table[y][x] - 255
                self.error_table[y][x + 1] += int(8 / 32 * current_error)
                self.error_table[y][x + 2] += int(4 / 32 * current_error)
                self.error_table[y + 1][x] += int(8 / 32 * current_error)
                self.error_table[y + 1][x + 1] += int(4 / 32 * current_error)
                self.error_table[y + 1][x + 2] += int(2 / 32 * current_error)
                self.error_table[y + 1][x - 1] += int(4 / 32 * current_error)
                self.error_table[y + 1][x - 2] += int(2 / 32 * current_error)


if __name__ == "__main__":
    
    burkes_instances = [
        Burkes(imread("image_data/lena.jpg", 1), threshold)
        for threshold in (1, 126, 130, 140)
    ]

    for burkes in burkes_instances:
        burkes.process()

    for burkes in burkes_instances:
        imshow(
            f"Original image with dithering threshold: {burkes.threshold}",
            burkes.output_img,
        )

    waitKey(0)
    destroyAllWindows()
