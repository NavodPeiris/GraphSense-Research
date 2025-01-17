

def __get_demo_graph(index):
    return [
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3, 5],
            3: [2, 4],
            4: [3],
            5: [2, 6, 8],
            6: [5, 7],
            7: [6, 8],
            8: [5, 7],
        },
        {
            0: [6],
            1: [9],
            2: [4, 5],
            3: [4],
            4: [2, 3],
            5: [2],
            6: [0, 7],
            7: [6],
            8: [],
            9: [1],
        },
        {
            0: [4],
            1: [6],
            2: [],
            3: [5, 6, 7],
            4: [0, 6],
            5: [3, 8, 9],
            6: [1, 3, 4, 7],
            7: [3, 6, 8, 9],
            8: [5, 7],
            9: [5, 7],
        },
        {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 3, 4],
            3: [0, 2, 4],
            4: [1, 2, 3],
        },
    ][index]


def compute_bridges(graph: dict[int, list[int]]) -> list[tuple[int, int]]:

    id_ = 0
    n = len(graph)  
    low = [0] * n
    visited = [False] * n

    def dfs(at, parent, bridges, id_):
        visited[at] = True
        low[at] = id_
        id_ += 1
        for to in graph[at]:
            if to == parent:
                pass
            elif not visited[to]:
                dfs(to, at, bridges, id_)
                low[at] = min(low[at], low[to])
                if id_ <= low[to]:
                    bridges.append((at, to) if at < to else (to, at))
            else:
                
                low[at] = min(low[at], low[to])

    bridges: list[tuple[int, int]] = []
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, bridges, id_)
    return bridges


if __name__ == "__main__":
    import doctest

    doctest.testmod()
