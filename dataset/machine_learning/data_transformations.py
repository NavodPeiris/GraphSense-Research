
from statistics import mean, stdev


def normalization(data: list, ndigits: int = 3) -> list:
    
    x_min = min(data)
    x_max = max(data)
    
    return [round((x - x_min) / (x_max - x_min), ndigits) for x in data]


def standardization(data: list, ndigits: int = 3) -> list:
    
    mu = mean(data)
    sigma = stdev(data)
    
    return [round((x - mu) / (sigma), ndigits) for x in data]
