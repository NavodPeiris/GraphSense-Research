from __future__ import annotations

import random


class Dice:
    NUM_SIDES = 6

    def __init__(self):
        self.sides = list(range(1, Dice.NUM_SIDES + 1))

    def roll(self):
        return random.choice(self.sides)


def throw_dice(num_throws: int, num_dice: int = 2) -> list[float]:
    dices = [Dice() for i in range(num_dice)]
    count_of_sum = [0] * (len(dices) * Dice.NUM_SIDES + 1)
    for _ in range(num_throws):
        count_of_sum[sum(dice.roll() for dice in dices)] += 1
    probability = [round((count * 100) / num_throws, 2) for count in count_of_sum]
    return probability[num_dice:]  


if __name__ == "__main__":
    import doctest

    doctest.testmod()
