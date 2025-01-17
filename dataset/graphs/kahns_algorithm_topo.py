def topological_sort(graph: dict[int, list[int]]) -> list[int] | None:

    indegree = [0] * len(graph)
    queue = []
    topo_order = []
    processed_vertices_count = 0

    
    for values in graph.values():
        for i in values:
            indegree[i] += 1

    
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    
    while queue:
        vertex = queue.pop(0)
        processed_vertices_count += 1
        topo_order.append(vertex)

        
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if processed_vertices_count != len(graph):
        return None  
    return topo_order  


if __name__ == "__main__":
    import doctest

    doctest.testmod()
