


def encrypt(input_string: str, key: int) -> str:
    
    temp_grid: list[list[str]] = [[] for _ in range(key)]
    lowest = key - 1

    if key <= 0:
        raise ValueError("Height of grid can't be 0 or negative")
    if key == 1 or len(input_string) <= key:
        return input_string

    for position, character in enumerate(input_string):
        num = position % (lowest * 2)  
        num = min(num, lowest * 2 - num)  
        temp_grid[num].append(character)
    grid = ["".join(row) for row in temp_grid]
    output_string = "".join(grid)

    return output_string


def decrypt(input_string: str, key: int) -> str:
    
    grid = []
    lowest = key - 1

    if key <= 0:
        raise ValueError("Height of grid can't be 0 or negative")
    if key == 1:
        return input_string

    temp_grid: list[list[str]] = [[] for _ in range(key)]  
    for position in range(len(input_string)):
        num = position % (lowest * 2)  
        num = min(num, lowest * 2 - num)  
        temp_grid[num].append("*")

    counter = 0
    for row in temp_grid:  
        splice = input_string[counter : counter + len(row)]
        grid.append(list(splice))
        counter += len(row)

    output_string = ""  
    for position in range(len(input_string)):
        num = position % (lowest * 2)  
        num = min(num, lowest * 2 - num)  
        output_string += grid[num][0]
        grid[num].pop(0)
    return output_string


def bruteforce(input_string: str) -> dict[int, str]:
    
    results = {}
    for key_guess in range(1, len(input_string)):  
        results[key_guess] = decrypt(input_string, key_guess)
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
