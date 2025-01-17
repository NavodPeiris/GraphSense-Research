

def valid_coloring(
    neighbours: list[int], colored_vertices: list[int], color: int
) -> bool:
    
    
    return not any(
        neighbour == 1 and colored_vertices[i] == color
        for i, neighbour in enumerate(neighbours)
    )


def util_color(
    graph: list[list[int]], max_colors: int, colored_vertices: list[int], index: int
) -> bool:
    
    if index == len(graph):
        return True

    
    for i in range(max_colors):
        if valid_coloring(graph[index], colored_vertices, i):
            
            colored_vertices[index] = i
            
            if util_color(graph, max_colors, colored_vertices, index + 1):
                return True
            
            colored_vertices[index] = -1
    return False


def color(graph: list[list[int]], max_colors: int) -> list[int]:
    
    colored_vertices = [-1] * len(graph)

    if util_color(graph, max_colors, colored_vertices, 0):
        return colored_vertices

    return []
