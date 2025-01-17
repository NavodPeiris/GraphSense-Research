

def prefix_function(input_string: str) -> list:

    
    prefix_result = [0] * len(input_string)

    for i in range(1, len(input_string)):
        
        j = prefix_result[i - 1]
        while j > 0 and input_string[i] != input_string[j]:
            j = prefix_result[j - 1]

        if input_string[i] == input_string[j]:
            j += 1
        prefix_result[i] = j

    return prefix_result


def longest_prefix(input_str: str) -> int:

    
    return max(prefix_function(input_str))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
