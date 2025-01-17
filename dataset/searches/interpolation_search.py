

def interpolation_search(sorted_collection: list[int], item: int) -> int | None:
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        
        if sorted_collection[left] == sorted_collection[right]:
            if sorted_collection[left] == item:
                return left
            return None

        point = left + ((item - sorted_collection[left]) * (right - left)) // (
            sorted_collection[right] - sorted_collection[left]
        )

        
        if point < 0 or point >= len(sorted_collection):
            return None

        current_item = sorted_collection[point]
        if current_item == item:
            return point
        if point < left:
            right = left
            left = point
        elif point > right:
            left = right
            right = point
        elif item < current_item:
            right = point - 1
        else:
            left = point + 1
    return None


def interpolation_search_by_recursion(
    sorted_collection: list[int], item: int, left: int = 0, right: int | None = None
) -> int | None:
    if right is None:
        right = len(sorted_collection) - 1
    
    if sorted_collection[left] == sorted_collection[right]:
        if sorted_collection[left] == item:
            return left
        return None

    point = left + ((item - sorted_collection[left]) * (right - left)) // (
        sorted_collection[right] - sorted_collection[left]
    )

    
    if point < 0 or point >= len(sorted_collection):
        return None

    if sorted_collection[point] == item:
        return point
    if point < left:
        return interpolation_search_by_recursion(sorted_collection, item, point, left)
    if point > right:
        return interpolation_search_by_recursion(sorted_collection, item, right, left)
    if sorted_collection[point] > item:
        return interpolation_search_by_recursion(
            sorted_collection, item, left, point - 1
        )
    return interpolation_search_by_recursion(sorted_collection, item, point + 1, right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
