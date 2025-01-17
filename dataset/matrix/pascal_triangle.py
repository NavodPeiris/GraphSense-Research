

def print_pascal_triangle(num_rows: int) -> None:
    triangle = generate_pascal_triangle(num_rows)
    for row_idx in range(num_rows):
        
        for _ in range(num_rows - row_idx - 1):
            print(end=" ")
        
        for col_idx in range(row_idx + 1):
            if col_idx != row_idx:
                print(triangle[row_idx][col_idx], end=" ")
            else:
                print(triangle[row_idx][col_idx], end="")
        print()


def generate_pascal_triangle(num_rows: int) -> list[list[int]]:

    if not isinstance(num_rows, int):
        raise TypeError("The input value of 'num_rows' should be 'int'")

    if num_rows == 0:
        return []
    elif num_rows < 0:
        raise ValueError(
            "The input value of 'num_rows' should be greater than or equal to 0"
        )

    triangle: list[list[int]] = []
    for current_row_idx in range(num_rows):
        current_row = populate_current_row(triangle, current_row_idx)
        triangle.append(current_row)
    return triangle


def populate_current_row(triangle: list[list[int]], current_row_idx: int) -> list[int]:
    current_row = [-1] * (current_row_idx + 1)
    
    current_row[0], current_row[-1] = 1, 1
    for current_col_idx in range(1, current_row_idx):
        calculate_current_element(
            triangle, current_row, current_row_idx, current_col_idx
        )
    return current_row


def calculate_current_element(
    triangle: list[list[int]],
    current_row: list[int],
    current_row_idx: int,
    current_col_idx: int,
) -> None:
    above_to_left_elt = triangle[current_row_idx - 1][current_col_idx - 1]
    above_to_right_elt = triangle[current_row_idx - 1][current_col_idx]
    current_row[current_col_idx] = above_to_left_elt + above_to_right_elt


def generate_pascal_triangle_optimized(num_rows: int) -> list[list[int]]:

    if not isinstance(num_rows, int):
        raise TypeError("The input value of 'num_rows' should be 'int'")

    if num_rows == 0:
        return []
    elif num_rows < 0:
        raise ValueError(
            "The input value of 'num_rows' should be greater than or equal to 0"
        )

    result: list[list[int]] = [[1]]

    for row_index in range(1, num_rows):
        temp_row = [0] + result[-1] + [0]
        row_length = row_index + 1
        
        distinct_elements = sum(divmod(row_length, 2))
        row_first_half = [
            temp_row[i - 1] + temp_row[i] for i in range(1, distinct_elements + 1)
        ]
        row_second_half = row_first_half[: (row_index + 1) // 2]
        row_second_half.reverse()
        row = row_first_half + row_second_half
        result.append(row)

    return result


def benchmark() -> None:
    from collections.abc import Callable
    from timeit import timeit

    def benchmark_a_function(func: Callable, value: int) -> None:
        call = f"{func.__name__}({value})"
        timing = timeit(f"__main__.{call}", setup="import __main__")
        
        print(f"{call:38} -- {timing:.4f} seconds")

    for value in range(15):  
        for func in (generate_pascal_triangle, generate_pascal_triangle_optimized):
            benchmark_a_function(func, value)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
