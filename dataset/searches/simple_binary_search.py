
from __future__ import annotations


def binary_search(a_list: list[int], item: int) -> bool:
    if len(a_list) == 0:
        return False
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    if item < a_list[midpoint]:
        return binary_search(a_list[:midpoint], item)
    else:
        return binary_search(a_list[midpoint + 1 :], item)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]
    target = int(input("Enter the number to be found in the list:\n").strip())
    not_str = "" if binary_search(sequence, target) else "not "
    print(f"{target} was {not_str}found in {sequence}")
