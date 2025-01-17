__author__ = "Tobias Carryer"

from time import time


class LinearCongruentialGenerator:

    
    
    
    
    

    def __init__(self, multiplier, increment, modulo, seed=int(time())):  
        self.multiplier = multiplier
        self.increment = increment
        self.modulo = modulo
        self.seed = seed

    def next_number(self):
        self.seed = (self.multiplier * self.seed + self.increment) % self.modulo
        return self.seed


if __name__ == "__main__":
    
    lcg = LinearCongruentialGenerator(1664525, 1013904223, 2 << 31)
    while True:
        print(lcg.next_number())
