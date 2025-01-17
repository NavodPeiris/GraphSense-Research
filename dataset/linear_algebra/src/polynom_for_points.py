def points_to_polynomial(coordinates: list[list[int]]) -> str:
    if len(coordinates) == 0 or not all(len(pair) == 2 for pair in coordinates):
        raise ValueError("The program cannot work out a fitting polynomial.")

    if len({tuple(pair) for pair in coordinates}) != len(coordinates):
        raise ValueError("The program cannot work out a fitting polynomial.")

    set_x = {x for x, _ in coordinates}
    if len(set_x) == 1:
        return f"x={coordinates[0][0]}"

    if len(set_x) != len(coordinates):
        raise ValueError("The program cannot work out a fitting polynomial.")

    x = len(coordinates)

    
    matrix: list[list[float]] = [
        [
            coordinates[count_of_line][0] ** (x - (count_in_line + 1))
            for count_in_line in range(x)
        ]
        for count_of_line in range(x)
    ]

    
    vector: list[float] = [coordinates[count_of_line][1] for count_of_line in range(x)]

    for count in range(x):
        for number in range(x):
            if count == number:
                continue
            fraction = matrix[number][count] / matrix[count][count]
            for counting_columns, item in enumerate(matrix[count]):
                
                matrix[number][counting_columns] -= item * fraction
            
            vector[number] -= vector[count] * fraction

    
    solution: list[str] = [
        str(vector[count] / matrix[count][count]) for count in range(x)
    ]

    solved = "f(x)="

    for count in range(x):
        remove_e: list[str] = solution[count].split("E")
        if len(remove_e) > 1:
            solution[count] = f"{remove_e[0]}*10^{remove_e[1]}"
        solved += f"x^{x - (count + 1)}*{solution[count]}"
        if count + 1 != x:
            solved += "+"

    return solved


if __name__ == "__main__":
    print(points_to_polynomial([]))
    print(points_to_polynomial([[]]))
    print(points_to_polynomial([[1, 0], [2, 0], [3, 0]]))
    print(points_to_polynomial([[1, 1], [2, 1], [3, 1]]))
    print(points_to_polynomial([[1, 3], [2, 3], [3, 3]]))
    print(points_to_polynomial([[1, 1], [2, 2], [3, 3]]))
    print(points_to_polynomial([[1, 1], [2, 4], [3, 9]]))
    print(points_to_polynomial([[1, 3], [2, 6], [3, 11]]))
    print(points_to_polynomial([[1, -3], [2, -6], [3, -11]]))
    print(points_to_polynomial([[1, 5], [2, 2], [3, 9]]))
