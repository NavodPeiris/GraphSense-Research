

def matching_min_vertex_cover(graph: dict) -> set:
    
    chosen_vertices = set()
    
    edges = get_edges(graph)

    
    
    
    while edges:
        from_node, to_node = edges.pop()
        chosen_vertices.add(from_node)
        chosen_vertices.add(to_node)
        for edge in edges.copy():
            if from_node in edge or to_node in edge:
                edges.discard(edge)
    return chosen_vertices


def get_edges(graph: dict) -> set:
    edges = set()
    for from_node, to_nodes in graph.items():
        for to_node in to_nodes:
            edges.add((from_node, to_node))
    return edges


if __name__ == "__main__":
    import doctest

    doctest.testmod()
