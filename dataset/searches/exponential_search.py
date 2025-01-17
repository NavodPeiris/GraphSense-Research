


from __future__ import annotations


def binary_search_by_recursion(
    sorted_collection: list[int], item: int, left: int = 0, right: int = -1
) -> int:
    if right < 0:
        right = len(sorted_collection) - 1
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    if right < left:
        return -1

    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint - 1)
    else:
        return binary_search_by_recursion(sorted_collection, item, midpoint + 1, right)


def exponential_search(sorted_collection: list[int], item: int) -> int:
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")

    if sorted_collection[0] == item:
        return 0

    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        bound *= 2

    left = bound // 2
    right = min(bound, len(sorted_collection) - 1)
    return binary_search_by_recursion(sorted_collection, item, left, right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    
    user_input = input("Enter numbers separated by commas: ").strip()
    collection = sorted(int(item) for item in user_input.split(","))
    target = int(input("Enter a number to search for: "))
    result = exponential_search(sorted_collection=collection, item=target)
    if result == -1:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at index {result} in {collection}.")
