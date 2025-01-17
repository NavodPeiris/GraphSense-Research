

def set_bit(number: int, position: int) -> int:
    
    return number | (1 << position)


def clear_bit(number: int, position: int) -> int:
    
    return number & ~(1 << position)


def flip_bit(number: int, position: int) -> int:
    
    return number ^ (1 << position)


def is_bit_set(number: int, position: int) -> bool:

    return ((number >> position) & 1) == 1


def get_bit(number: int, position: int) -> int:
    
    return int((number & (1 << position)) != 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
