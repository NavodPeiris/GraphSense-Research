from __future__ import annotations


def median(nums: list) -> int | float:
    
    
    sorted_list: list[int] = sorted(nums)
    length = len(sorted_list)
    mid_index = length >> 1
    return (
        (sorted_list[mid_index] + sorted_list[mid_index - 1]) / 2
        if length % 2 == 0
        else sorted_list[mid_index]
    )


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
