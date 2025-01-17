from collections import defaultdict, deque


def is_bipartite_dfs(graph: defaultdict[int, list[int]]) -> bool:

    def depth_first_search(node: int, color: int) -> bool:
        if visited[node] == -1:
            visited[node] = color
            for neighbor in graph[node]:
                if not depth_first_search(neighbor, 1 - color):
                    return False
        return visited[node] == color

    visited: defaultdict[int, int] = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1 and not depth_first_search(node, 0):
            return False
    return True


def is_bipartite_bfs(graph: defaultdict[int, list[int]]) -> bool:
    visited: defaultdict[int, int] = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1:
            queue: deque[int] = deque()
            queue.append(node)
            visited[node] = 0
            while queue:
                curr_node = queue.popleft()
                for neighbor in graph[curr_node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1 - visited[curr_node]
                        queue.append(neighbor)
                    elif visited[neighbor] == visited[curr_node]:
                        return False
    return True


if __name__ == "__main":
    import doctest

    result = doctest.testmod()
    if result.failed:
        print(f"{result.failed} test(s) failed.")
    else:
        print("All tests passed!")
