

from __future__ import annotations

test_array = [2, 1, 4, 5, 6, 0, 8, 9, 1, 2, 0, 6, 4, 2, 0, 6, 5, 3, 2, 7]


class Node:
    def __init__(self, length: int) -> None:
        self.minn: int = -1
        self.maxx: int = -1
        self.map_left: list[int] = [-1] * length
        self.left: Node | None = None
        self.right: Node | None = None

    def __repr__(self) -> str:
      
        return f"Node(min_value={self.minn} max_value={self.maxx})"


def build_tree(arr: list[int]) -> Node | None:
    
    root = Node(len(arr))
    root.minn, root.maxx = min(arr), max(arr)
    
    if root.minn == root.maxx:
        return root
    
    pivot = (root.minn + root.maxx) // 2

    left_arr: list[int] = []
    right_arr: list[int] = []

    for index, num in enumerate(arr):
        if num <= pivot:
            left_arr.append(num)
        else:
            right_arr.append(num)
        root.map_left[index] = len(left_arr)
    root.left = build_tree(left_arr)
    root.right = build_tree(right_arr)
    return root


def rank_till_index(node: Node | None, num: int, index: int) -> int:
    
    if index < 0 or node is None:
        return 0
    
    if node.minn == node.maxx:
        return index + 1 if node.minn == num else 0
    pivot = (node.minn + node.maxx) // 2
    if num <= pivot:
        
        return rank_till_index(node.left, num, node.map_left[index] - 1)
    else:
        
        return rank_till_index(node.right, num, index - node.map_left[index])


def rank(node: Node | None, num: int, start: int, end: int) -> int:
    
    if start > end:
        return 0
    rank_till_end = rank_till_index(node, num, end)
    rank_before_start = rank_till_index(node, num, start - 1)
    return rank_till_end - rank_before_start


def quantile(node: Node | None, index: int, start: int, end: int) -> int:
    
    if index > (end - start) or start > end or node is None:
        return -1
    
    if node.minn == node.maxx:
        return node.minn
    
    num_elements_in_left_tree = node.map_left[end] - (
        node.map_left[start - 1] if start else 0
    )
    if num_elements_in_left_tree > index:
        return quantile(
            node.left,
            index,
            (node.map_left[start - 1] if start else 0),
            node.map_left[end] - 1,
        )
    else:
        return quantile(
            node.right,
            index - num_elements_in_left_tree,
            start - (node.map_left[start - 1] if start else 0),
            end - node.map_left[end],
        )


def range_counting(
    node: Node | None, start: int, end: int, start_num: int, end_num: int
) -> int:
    
    if (
        start > end
        or node is None
        or start_num > end_num
        or node.minn > end_num
        or node.maxx < start_num
    ):
        return 0
    if start_num <= node.minn and node.maxx <= end_num:
        return end - start + 1
    left = range_counting(
        node.left,
        (node.map_left[start - 1] if start else 0),
        node.map_left[end] - 1,
        start_num,
        end_num,
    )
    right = range_counting(
        node.right,
        start - (node.map_left[start - 1] if start else 0),
        end - node.map_left[end],
        start_num,
        end_num,
    )
    return left + right


if __name__ == "__main__":
    import doctest

    doctest.testmod()
