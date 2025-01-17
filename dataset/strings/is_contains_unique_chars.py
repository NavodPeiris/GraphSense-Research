def is_contains_unique_chars(input_str: str) -> bool:

    
    
    
    bitmap = 0
    for ch in input_str:
        ch_unicode = ord(ch)
        ch_bit_index_on = pow(2, ch_unicode)

        
        if bitmap >> ch_unicode & 1 == 1:
            return False
        bitmap |= ch_bit_index_on
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
