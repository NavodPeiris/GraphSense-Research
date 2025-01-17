
test_graph_1 = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1], 4: [5, 6], 5: [4, 6], 6: [4, 5]}

test_graph_2 = {0: [1, 2, 3], 1: [0, 3], 2: [0], 3: [0, 1], 4: [], 5: []}


def dfs(graph: dict, vert: int, visited: list) -> list:

    visited[vert] = True
    connected_verts = []

    for neighbour in graph[vert]:
        if not visited[neighbour]:
            connected_verts += dfs(graph, neighbour, visited)

    return [vert, *connected_verts]


def connected_components(graph: dict) -> list:

    graph_size = len(graph)
    visited = graph_size * [False]
    components_list = []

    for i in range(graph_size):
        if not visited[i]:
            i_connected = dfs(graph, i, visited)
            components_list.append(i_connected)

    return components_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
