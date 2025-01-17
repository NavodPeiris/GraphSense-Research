
import numpy as np
from cv2 import destroyAllWindows, imread, imshow, waitKey


class NearestNeighbour:

    def __init__(self, img, dst_width: int, dst_height: int):
        if dst_width < 0 or dst_height < 0:
            raise ValueError("Destination width/height should be > 0")

        self.img = img
        self.src_w = img.shape[1]
        self.src_h = img.shape[0]
        self.dst_w = dst_width
        self.dst_h = dst_height

        self.ratio_x = self.src_w / self.dst_w
        self.ratio_y = self.src_h / self.dst_h

        self.output = self.output_img = (
            np.ones((self.dst_h, self.dst_w, 3), np.uint8) * 255
        )

    def process(self):
        for i in range(self.dst_h):
            for j in range(self.dst_w):
                self.output[i][j] = self.img[self.get_y(i)][self.get_x(j)]

    def get_x(self, x: int) -> int:
        return int(self.ratio_x * x)

    def get_y(self, y: int) -> int:
        return int(self.ratio_y * y)


if __name__ == "__main__":
    dst_w, dst_h = 800, 600
    im = imread("image_data/lena.jpg", 1)
    n = NearestNeighbour(im, dst_w, dst_h)
    n.process()

    imshow(
        f"Image resized from: {im.shape[1]}x{im.shape[0]} to {dst_w}x{dst_h}", n.output
    )
    waitKey(0)
    destroyAllWindows()
