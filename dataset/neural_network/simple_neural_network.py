
import math
import random



def sigmoid_function(value: float, deriv: bool = False) -> float:
    if deriv:
        return value * (1 - value)
    return 1 / (1 + math.exp(-value))



INITIAL_VALUE = 0.02


def forward_propagation(expected: int, number_propagations: int) -> float:

    
    weight = float(2 * (random.randint(1, 100)) - 1)

    for _ in range(number_propagations):
        
        layer_1 = sigmoid_function(INITIAL_VALUE * weight)
        
        layer_1_error = (expected / 100) - layer_1
        
        layer_1_delta = layer_1_error * sigmoid_function(layer_1, True)
        
        weight += INITIAL_VALUE * layer_1_delta

    return layer_1 * 100


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    expected = int(input("Expected value: "))
    number_propagations = int(input("Number of propagations: "))
    print(forward_propagation(expected, number_propagations))
