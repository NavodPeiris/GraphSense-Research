
from PIL import Image


def change_contrast(img: Image, level: int) -> Image:
    factor = (259 * (level + 255)) / (255 * (259 - level))

    def contrast(c: int) -> int:
        return int(128 + factor * (c - 128))

    return img.point(contrast)


if __name__ == "__main__":
    
    with Image.open("image_data/lena.jpg") as img:
        
        cont_img = change_contrast(img, 170)
        cont_img.save("image_data/lena_high_contrast.png", format="png")
