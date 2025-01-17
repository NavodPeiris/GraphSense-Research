
test_graph_1 = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}

test_graph_2 = {0: [1, 2, 3], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}


def topology_sort(
    graph: dict[int, list[int]], vert: int, visited: list[bool]
) -> list[int]:

    visited[vert] = True
    order = []

    for neighbour in graph[vert]:
        if not visited[neighbour]:
            order += topology_sort(graph, neighbour, visited)

    order.append(vert)

    return order


def find_components(
    reversed_graph: dict[int, list[int]], vert: int, visited: list[bool]
) -> list[int]:

    visited[vert] = True
    component = [vert]

    for neighbour in reversed_graph[vert]:
        if not visited[neighbour]:
            component += find_components(reversed_graph, neighbour, visited)

    return component


def strongly_connected_components(graph: dict[int, list[int]]) -> list[list[int]]:

    visited = len(graph) * [False]
    reversed_graph: dict[int, list[int]] = {vert: [] for vert in range(len(graph))}

    for vert, neighbours in graph.items():
        for neighbour in neighbours:
            reversed_graph[neighbour].append(vert)

    order = []
    for i, was_visited in enumerate(visited):
        if not was_visited:
            order += topology_sort(graph, i, visited)

    components_list = []
    visited = len(graph) * [False]

    for i in range(len(graph)):
        vert = order[len(graph) - i - 1]
        if not visited[vert]:
            component = find_components(reversed_graph, vert, visited)
            components_list.append(component)

    return components_list
