
import sys
import turtle


def get_mid(p1: tuple[float, float], p2: tuple[float, float]) -> tuple[float, float]:
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def triangle(
    vertex1: tuple[float, float],
    vertex2: tuple[float, float],
    vertex3: tuple[float, float],
    depth: int,
) -> None:
    my_pen.up()
    my_pen.goto(vertex1[0], vertex1[1])
    my_pen.down()
    my_pen.goto(vertex2[0], vertex2[1])
    my_pen.goto(vertex3[0], vertex3[1])
    my_pen.goto(vertex1[0], vertex1[1])

    if depth == 0:
        return

    triangle(vertex1, get_mid(vertex1, vertex2), get_mid(vertex1, vertex3), depth - 1)
    triangle(vertex2, get_mid(vertex1, vertex2), get_mid(vertex2, vertex3), depth - 1)
    triangle(vertex3, get_mid(vertex3, vertex2), get_mid(vertex1, vertex3), depth - 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError(
            "Correct format for using this script: "
            "python fractals.py <int:depth_for_fractal>"
        )
    my_pen = turtle.Turtle()
    my_pen.ht()
    my_pen.speed(5)
    my_pen.pencolor("red")

    vertices = [(-175, -125), (0, 175), (175, -125)]  
    triangle(vertices[0], vertices[1], vertices[2], int(sys.argv[1]))
    turtle.Screen().exitonclick()
