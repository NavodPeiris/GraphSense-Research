from PIL import Image


def change_brightness(img: Image, level: float) -> Image:

    def brightness(c: int) -> float:
        return 128 + level + (c - 128)

    if not -255.0 <= level <= 255.0:
        raise ValueError("level must be between -255.0 (black) and 255.0 (white)")
    return img.point(brightness)


if __name__ == "__main__":
    
    with Image.open("image_data/lena.jpg") as img:
        
        brigt_img = change_brightness(img, 100)
        brigt_img.save("image_data/lena_brightness.png", format="png")
