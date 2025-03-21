

def simplify(current_set: list[list]) -> list[list]:
    
    duplicate_set = current_set.copy()
    for row_index, row in enumerate(duplicate_set):
        magnitude = row[0]
        for column_index, column in enumerate(row):
            if magnitude == 0:
                current_set[row_index][column_index] = column
                continue
            current_set[row_index][column_index] = column / magnitude
    
    first_row = current_set[0]
    final_set = [first_row]
    current_set = current_set[1::]
    for row in current_set:
        temp_row = []
        
        if row[0] == 0:
            final_set.append(row)
            continue
        for column_index in range(len(row)):
            temp_row.append(first_row[column_index] - row[column_index])
        final_set.append(temp_row)
    
    if len(final_set[0]) != 3:
        current_first_row = final_set[0]
        current_first_column = []
        next_iteration = []
        for row in final_set[1::]:
            current_first_column.append(row[0])
            next_iteration.append(row[1::])
        resultant = simplify(next_iteration)
        for i in range(len(resultant)):
            resultant[i].insert(0, current_first_column[i])
        resultant.insert(0, current_first_row)
        final_set = resultant
    return final_set


def solve_simultaneous(equations: list[list]) -> list:
    if len(equations) == 0:
        raise IndexError("solve_simultaneous() requires n lists of length n+1")
    _length = len(equations) + 1
    if any(len(item) != _length for item in equations):
        raise IndexError("solve_simultaneous() requires n lists of length n+1")
    for row in equations:
        if any(not isinstance(column, (int, float)) for column in row):
            raise ValueError("solve_simultaneous() requires lists of integers")
    if len(equations) == 1:
        return [equations[0][-1] / equations[0][0]]
    data_set = equations.copy()
    if any(0 in row for row in data_set):
        temp_data = data_set.copy()
        full_row = []
        for row_index, row in enumerate(temp_data):
            if 0 not in row:
                full_row = data_set.pop(row_index)
                break
        if not full_row:
            raise ValueError("solve_simultaneous() requires at least 1 full equation")
        data_set.insert(0, full_row)
    useable_form = data_set.copy()
    simplified = simplify(useable_form)
    simplified = simplified[::-1]
    solutions: list = []
    for row in simplified:
        current_solution = row[-1]
        if not solutions:
            if row[-2] == 0:
                solutions.append(0)
                continue
            solutions.append(current_solution / row[-2])
            continue
        temp_row = row.copy()[: len(row) - 1 :]
        while temp_row[0] == 0:
            temp_row.pop(0)
        if len(temp_row) == 0:
            solutions.append(0)
            continue
        temp_row = temp_row[1::]
        temp_row = temp_row[::-1]
        for column_index, column in enumerate(temp_row):
            current_solution -= column * solutions[column_index]
        solutions.append(current_solution)
    final = []
    for item in solutions:
        final.append(float(round(item, 5)))
    return final[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    eq = [
        [2, 1, 1, 1, 1, 4],
        [1, 2, 1, 1, 1, 5],
        [1, 1, 2, 1, 1, 6],
        [1, 1, 1, 2, 1, 7],
        [1, 1, 1, 1, 2, 8],
    ]
    print(solve_simultaneous(eq))
    print(solve_simultaneous([[4, 2]]))
