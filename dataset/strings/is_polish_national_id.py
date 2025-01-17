def is_polish_national_id(input_str: str) -> bool:

    
    if not isinstance(input_str, str):
        msg = f"Expected str as input, found {type(input_str)}"
        raise ValueError(msg)

    
    try:
        input_int = int(input_str)
    except ValueError:
        msg = "Expected number as input"
        raise ValueError(msg)

    
    if not 10100000 <= input_int <= 99923199999:
        return False

    
    month = int(input_str[2:4])

    if (
        month not in range(1, 13)  
        and month not in range(21, 33)  
        and month not in range(41, 53)  
        and month not in range(61, 73)  
        and month not in range(81, 93)  
    ):
        return False

    
    day = int(input_str[4:6])

    if day not in range(1, 32):
        return False

    
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    subtotal = 0

    digits_to_check = str(input_str)[:-1]  

    for index, digit in enumerate(digits_to_check):
        
        
        subtotal += (int(digit) * multipliers[index]) % 10

    checksum = 10 - subtotal % 10

    return checksum == input_int % 10


if __name__ == "__main__":
    from doctest import testmod

    testmod()
