
from heapq import heappop, heappush
from sys import maxsize


def smallest_range(nums: list[list[int]]) -> list[int]:

    min_heap: list[tuple[int, int, int]] = []
    current_max = -maxsize - 1

    for i, items in enumerate(nums):
        heappush(min_heap, (items[0], i, 0))
        current_max = max(current_max, items[0])

    
    smallest_range = [-maxsize - 1, maxsize]

    while min_heap:
        current_min, list_index, element_index = heappop(min_heap)

        if current_max - current_min < smallest_range[1] - smallest_range[0]:
            smallest_range = [current_min, current_max]

        if element_index == len(nums[list_index]) - 1:
            break

        next_element = nums[list_index][element_index + 1]
        heappush(min_heap, (next_element, list_index, element_index + 1))
        current_max = max(current_max, next_element)

    return smallest_range


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]])}")
