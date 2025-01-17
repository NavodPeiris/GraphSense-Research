def gray_code(bit_count: int) -> list:
    
    if bit_count < 0:
        raise ValueError("The given input must be positive")


    sequence = gray_code_sequence_string(bit_count)
    
    for i in range(len(sequence)):
        sequence[i] = int(sequence[i], 2)

    return sequence


def gray_code_sequence_string(bit_count: int) -> list:
    
    if bit_count == 0:
        return ["0"]

    if bit_count == 1:
        return ["0", "1"]

    seq_len = 1 << bit_count  
    

   
    smaller_sequence = gray_code_sequence_string(bit_count - 1)

    sequence = []

    
    for i in range(seq_len // 2):
        generated_no = "0" + smaller_sequence[i]
        sequence.append(generated_no)

    
    for i in reversed(range(seq_len // 2)):
        generated_no = "1" + smaller_sequence[i]
        sequence.append(generated_no)

    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
