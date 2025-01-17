
import colorsys

from PIL import Image


def get_distance(x: float, y: float, max_step: int) -> float:
    a = x
    b = y
    for step in range(max_step):  
        a_new = a * a - b * b + x
        b = 2 * a * b + y
        a = a_new

        
        
        if a * a + b * b > 4:
            break
    return step / (max_step - 1)


def get_black_and_white_rgb(distance: float) -> tuple:
    if distance == 1:
        return (0, 0, 0)
    else:
        return (255, 255, 255)


def get_color_coded_rgb(distance: float) -> tuple:
    if distance == 1:
        return (0, 0, 0)
    else:
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(distance, 1, 1))


def get_image(
    image_width: int = 800,
    image_height: int = 600,
    figure_center_x: float = -0.6,
    figure_center_y: float = 0,
    figure_width: float = 3.2,
    max_step: int = 50,
    use_distance_color_coding: bool = True,
) -> Image.Image:
    img = Image.new("RGB", (image_width, image_height))
    pixels = img.load()

    
    for image_x in range(image_width):
        for image_y in range(image_height):
            
            figure_height = figure_width / image_width * image_height
            figure_x = figure_center_x + (image_x / image_width - 0.5) * figure_width
            figure_y = figure_center_y + (image_y / image_height - 0.5) * figure_height

            distance = get_distance(figure_x, figure_y, max_step)

            
            if use_distance_color_coding:
                pixels[image_x, image_y] = get_color_coded_rgb(distance)
            else:
                pixels[image_x, image_y] = get_black_and_white_rgb(distance)

    return img


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    
    img = get_image()

    
    
    

    
    

    
    

    img.show()
