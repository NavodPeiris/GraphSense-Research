

def product_sum(arr: list[int | list], depth: int) -> int:
    
    total_sum = 0
    for ele in arr:
        total_sum += product_sum(ele, depth + 1) if isinstance(ele, list) else ele
    return total_sum * depth


def product_sum_array(array: list[int | list]) -> int:
    
    return product_sum(array, 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
