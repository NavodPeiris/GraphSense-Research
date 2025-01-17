
import turtle


def draw_cross(x: float, y: float, length: float):
    turtle.up()
    turtle.goto(x - length / 2, y - length / 6)
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length / 3)
        turtle.right(90)
        turtle.fd(length / 3)
        turtle.left(90)
        turtle.fd(length / 3)
        turtle.left(90)
    turtle.end_fill()


def draw_fractal_recursive(x: float, y: float, length: float, depth: float):
    if depth == 0:
        draw_cross(x, y, length)
        return

    draw_fractal_recursive(x, y, length / 3, depth - 1)
    draw_fractal_recursive(x + length / 3, y, length / 3, depth - 1)
    draw_fractal_recursive(x - length / 3, y, length / 3, depth - 1)
    draw_fractal_recursive(x, y + length / 3, length / 3, depth - 1)
    draw_fractal_recursive(x, y - length / 3, length / 3, depth - 1)


def set_color(rgb: str):
    turtle.color(rgb)


def draw_vicsek_fractal(x: float, y: float, length: float, depth: float, color="blue"):
    turtle.speed(0)
    turtle.hideturtle()
    set_color(color)
    draw_fractal_recursive(x, y, length, depth)
    turtle.Screen().update()


def main():
    draw_vicsek_fractal(0, 0, 800, 4)

    turtle.done()


if __name__ == "__main__":
    main()
