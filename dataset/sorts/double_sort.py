from typing import Any


def double_sort(collection: list[Any]) -> list[Any]:
    no_of_elements = len(collection)
    for _ in range(
        int(((no_of_elements - 1) / 2) + 1)
    ):  
        for j in range(no_of_elements - 1):
            
            if collection[j + 1] < collection[j]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
            
            if collection[no_of_elements - 1 - j] < collection[no_of_elements - 2 - j]:
                (
                    collection[no_of_elements - 1 - j],
                    collection[no_of_elements - 2 - j],
                ) = (
                    collection[no_of_elements - 2 - j],
                    collection[no_of_elements - 1 - j],
                )
    return collection


if __name__ == "__main__":
    
    unsorted = [int(x) for x in input("Enter the list to be sorted: ").split() if x]
    print("the sorted list is")
    print(f"{double_sort(unsorted) = }")
