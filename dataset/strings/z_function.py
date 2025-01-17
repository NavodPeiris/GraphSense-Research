

def z_function(input_str: str) -> list[int]:
    z_result = [0 for i in range(len(input_str))]

    
    left_pointer, right_pointer = 0, 0

    for i in range(1, len(input_str)):
        
        if i <= right_pointer:
            min_edge = min(right_pointer - i + 1, z_result[i - left_pointer])
            z_result[i] = min_edge

        while go_next(i, z_result, input_str):
            z_result[i] += 1

        
        
        if i + z_result[i] - 1 > right_pointer:
            left_pointer, right_pointer = i, i + z_result[i] - 1

    return z_result


def go_next(i: int, z_result: list[int], s: str) -> bool:
    return i + z_result[i] < len(s) and s[z_result[i]] == s[i + z_result[i]]


def find_pattern(pattern: str, input_str: str) -> int:
    answer = 0
    
    
    z_result = z_function(pattern + input_str)

    for val in z_result:
        
        
        
        if val >= len(pattern):
            answer += 1

    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
