

def binary_insertion_sort(collection: list) -> list:

    n = len(collection)
    for i in range(1, n):
        value_to_insert = collection[i]
        low = 0
        high = i - 1

        while low <= high:
            mid = (low + high) // 2
            if value_to_insert < collection[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -1):
            collection[j] = collection[j - 1]
        collection[low] = value_to_insert
    return collection


if __name__ == "__main":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    try:
        unsorted = [int(item) for item in user_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
        raise
    print(f"{binary_insertion_sort(unsorted) = }")
