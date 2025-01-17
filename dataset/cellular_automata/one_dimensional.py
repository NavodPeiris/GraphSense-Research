
from __future__ import annotations

from PIL import Image


CELLS = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



def format_ruleset(ruleset: int) -> list[int]:
    
    return [int(c) for c in f"{ruleset:08}"[:8]]


def new_generation(cells: list[list[int]], rule: list[int], time: int) -> list[int]:
    population = len(cells[0])  
    next_generation = []
    for i in range(population):
        
        left_neighbor = 0 if i == 0 else cells[time][i - 1]
        right_neighbor = 0 if i == population - 1 else cells[time][i + 1]
        
        situation = 7 - int(f"{left_neighbor}{cells[time][i]}{right_neighbor}", 2)
        next_generation.append(rule[situation])
    return next_generation


def generate_image(cells: list[list[int]]) -> Image.Image:
    
    img = Image.new("RGB", (len(cells[0]), len(cells)))
    pixels = img.load()
    
    for w in range(img.width):
        for h in range(img.height):
            color = 255 - int(255 * cells[h][w])
            pixels[w, h] = (color, color, color)
    return img


if __name__ == "__main__":
    rule_num = bin(int(input("Rule:\n").strip()))[2:]
    rule = format_ruleset(int(rule_num))
    for time in range(16):
        CELLS.append(new_generation(CELLS, rule, time))
    img = generate_image(CELLS)
    
    img.show()
