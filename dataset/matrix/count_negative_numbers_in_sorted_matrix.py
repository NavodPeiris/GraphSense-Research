

def generate_large_matrix() -> list[list[int]]:
    return [list(range(1000 - i, -1000 - i, -1)) for i in range(1000)]


grid = generate_large_matrix()
test_grids = (
    [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
    [[3, 2], [1, 0]],
    [[7, 7, 6]],
    [[7, 7, 6], [-1, -2, -3]],
    grid,
)


def validate_grid(grid: list[list[int]]) -> None:
    assert all(row == sorted(row, reverse=True) for row in grid)
    assert all(list(col) == sorted(col, reverse=True) for col in zip(*grid))


def find_negative_index(array: list[int]) -> int:
    left = 0
    right = len(array) - 1

    
    if not array or array[0] < 0:
        return 0

    while right + 1 > left:
        mid = (left + right) // 2
        num = array[mid]

        
        if num < 0 and array[mid - 1] >= 0:
            return mid

        if num >= 0:
            left = mid + 1
        else:
            right = mid - 1
    
    return len(array)


def count_negatives_binary_search(grid: list[list[int]]) -> int:
    total = 0
    bound = len(grid[0])

    for i in range(len(grid)):
        bound = find_negative_index(grid[i][:bound])
        total += bound
    return (len(grid) * len(grid[0])) - total


def count_negatives_brute_force(grid: list[list[int]]) -> int:
    return len([number for row in grid for number in row if number < 0])


def count_negatives_brute_force_with_break(grid: list[list[int]]) -> int:
    total = 0
    for row in grid:
        for i, number in enumerate(row):
            if number < 0:
                total += len(row) - i
                break
    return total


def benchmark() -> None:
    from timeit import timeit

    print("Running benchmarks")
    setup = (
        "from __main__ import count_negatives_binary_search, "
        "count_negatives_brute_force, count_negatives_brute_force_with_break, grid"
    )
    for func in (
        "count_negatives_binary_search",  
        "count_negatives_brute_force_with_break",  
        "count_negatives_brute_force",  
    ):
        time = timeit(f"{func}(grid=grid)", setup=setup, number=500)
        print(f"{func}() took {time:0.4f} seconds")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
