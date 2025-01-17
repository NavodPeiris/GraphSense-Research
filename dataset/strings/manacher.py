def palindromic_string(input_string: str) -> str:
    max_length = 0

    
    new_input_string = ""
    output_string = ""

    
    for i in input_string[: len(input_string) - 1]:
        new_input_string += i + "|"
    
    new_input_string += input_string[-1]

    
    
    left, right = 0, 0

    
    length = [1 for i in range(len(new_input_string))]

    
    start = 0
    for j in range(len(new_input_string)):
        k = 1 if j > right else min(length[left + right - j] // 2, right - j + 1)
        while (
            j - k >= 0
            and j + k < len(new_input_string)
            and new_input_string[k + j] == new_input_string[j - k]
        ):
            k += 1

        length[j] = 2 * k - 1

        
        
        if j + k - 1 > right:
            left = j - k + 1
            right = j + k - 1

        
        if max_length < length[j]:
            max_length = length[j]
            start = j

    
    s = new_input_string[start - max_length // 2 : start + max_length // 2 + 1]
    for i in s:
        if i != "|":
            output_string += i

    return output_string


if __name__ == "__main__":
    import doctest

    doctest.testmod()
