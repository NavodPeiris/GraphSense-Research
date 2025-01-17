

from collections import defaultdict


def dfs(start: int) -> int:
    
    ret = 1
    visited[start] = True
    for v in tree[start]:
        if v not in visited:
            ret += dfs(v)
    if ret % 2 == 0:
        cuts.append(start)
    return ret


def even_tree():
    dfs(1)


if __name__ == "__main__":
    n, m = 10, 9
    tree = defaultdict(list)
    visited: dict[int, bool] = {}
    cuts: list[int] = []
    count = 0
    edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    even_tree()
    print(len(cuts) - 1)
