def get_reverse_bit_string(number: int) -> str:
    
    if not isinstance(number, int):
        msg = (
            "operation can not be conducted on a object of type "
            f"{type(number).__name__}"
        )
        raise TypeError(msg)
    bit_string = ""
    for _ in range(32):
        bit_string += str(number % 2)
        number = number >> 1
    return bit_string


def reverse_bit(number: int) -> str:
    
    if number < 0:
        raise ValueError("the value of input must be positive")
    elif isinstance(number, float):
        raise TypeError("Input value must be a 'int' type")
    elif isinstance(number, str):
        raise TypeError("'<' not supported between instances of 'str' and 'int'")
    result = 0
    
    for _ in range(1, 33):
        
        result = result << 1
        
        end_bit = number % 2
        
        number = number >> 1
        
        result = result | end_bit
    return get_reverse_bit_string(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
