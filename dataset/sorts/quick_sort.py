
from __future__ import annotations

from random import randrange


def quick_sort(collection: list) -> list:
    
    if len(collection) < 2:
        return collection

    
    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    
    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


if __name__ == "__main__":
    
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]

    
    print(quick_sort(unsorted))
