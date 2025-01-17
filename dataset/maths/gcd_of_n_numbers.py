
from collections import Counter


def get_factors(
    number: int, factors: Counter | None = None, factor: int = 2
) -> Counter:

    match number:
        case int(number) if number == 1:
            return Counter({1: 1})
        case int(num) if number > 0:
            number = num
        case _:
            raise TypeError("number must be integer and greater than zero")

    factors = factors or Counter()

    if number == factor:  
        
        factors[factor] += 1
        return factors

    if number % factor > 0:
        
        
        return get_factors(number, factors, factor + 1)

    factors[factor] += 1
    
    return get_factors(number // factor, factors, factor)


def get_greatest_common_divisor(*numbers: int) -> int:

    
    try:
        same_factors, *factors = map(get_factors, numbers)
    except TypeError as e:
        raise Exception("numbers must be integer and greater than zero") from e

    for factor in factors:
        same_factors &= factor
        
        

    
    mult = 1
    
    
    for m in [factor**power for factor, power in same_factors.items()]:
        mult *= m
    return mult


if __name__ == "__main__":
    print(get_greatest_common_divisor(18, 45))
