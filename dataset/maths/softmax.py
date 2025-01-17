
import numpy as np


def softmax(vector):

    
    
    exponent_vector = np.exp(vector)

    
    sum_of_exponents = np.sum(exponent_vector)

    
    softmax_vector = exponent_vector / sum_of_exponents

    return softmax_vector


if __name__ == "__main__":
    print(softmax((0,)))
