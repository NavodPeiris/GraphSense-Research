

import random
import sys

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

usage_doc = "Usage of script: script_name <size_of_canvas:int>"

choice = [0] * 100 + [1] * 10
random.shuffle(choice)


def create_canvas(size: int) -> list[list[bool]]:
    canvas = [[False for i in range(size)] for j in range(size)]
    return canvas


def seed(canvas: list[list[bool]]) -> None:
    for i, row in enumerate(canvas):
        for j, _ in enumerate(row):
            canvas[i][j] = bool(random.getrandbits(1))


def run(canvas: list[list[bool]]) -> list[list[bool]]:
    
    current_canvas = np.array(canvas)
    next_gen_canvas = np.array(create_canvas(current_canvas.shape[0]))
    for r, row in enumerate(current_canvas):
        for c, pt in enumerate(row):
            next_gen_canvas[r][c] = __judge_point(
                pt, current_canvas[r - 1 : r + 2, c - 1 : c + 2]
            )

    return next_gen_canvas.tolist()


def __judge_point(pt: bool, neighbours: list[list[bool]]) -> bool:
    dead = 0
    alive = 0
    
    for i in neighbours:
        for status in i:
            if status:
                alive += 1
            else:
                dead += 1

    
    if pt:
        alive -= 1
    else:
        dead -= 1

    
    state = pt
    if pt:
        if alive < 2:
            state = False
        elif alive in {2, 3}:
            state = True
        elif alive > 3:
            state = False
    elif alive == 3:
        state = True

    return state


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception(usage_doc)

    canvas_size = int(sys.argv[1])
    
    c = create_canvas(canvas_size)
    seed(c)
    fig, ax = plt.subplots()
    fig.show()
    cmap = ListedColormap(["w", "k"])
    try:
        while True:
            c = run(c)
            ax.matshow(c, cmap=cmap)
            fig.canvas.draw()
            ax.cla()
    except KeyboardInterrupt:
        
        pass
