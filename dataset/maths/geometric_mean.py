

def compute_geometric_mean(*args: int) -> float:
    product = 1
    for number in args:
        if not isinstance(number, int) and not isinstance(number, float):
            raise TypeError("Not a Number")
        product *= number
    
    
    if product < 0 and len(args) % 2 == 0:
        raise ArithmeticError("Cannot Compute Geometric Mean for these numbers.")
    mean = abs(product) ** (1 / len(args))
    
    if product < 0:
        mean = -mean
    
    possible_mean = float(round(mean))
    
    if possible_mean ** len(args) == product:
        mean = possible_mean
    return mean


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="compute_geometric_mean")
    print(compute_geometric_mean(-3, -27))
