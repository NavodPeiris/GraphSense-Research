

def bitap_string_match(text: str, pattern: str) -> int:
    if not pattern:
        return 0
    m = len(pattern)
    if m > len(text):
        return -1

    
    state = ~1
    
    pattern_mask: list[int] = [~0] * 27  

    for i, char in enumerate(pattern):
        
        
        pattern_index: int = ord(char) - ord("a")
        pattern_mask[pattern_index] &= ~(1 << i)

    for i, char in enumerate(text):
        text_index = ord(char) - ord("a")
        
        
        
        state |= pattern_mask[text_index]
        state <<= 1

        
        
        if (state & (1 << m)) == 0:
            return i - m + 1

    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
