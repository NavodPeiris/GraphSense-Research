
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]


def breadth_first_search(graph: list, source: int, sink: int, parents: list) -> bool:
    visited = [False] * len(graph)  
    queue = []  

    
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)  
        
        for ind, node in enumerate(graph[u]):
            if visited[ind] is False and node > 0:
                queue.append(ind)
                visited[ind] = True
                parents[ind] = u
    return visited[sink]


def ford_fulkerson(graph: list, source: int, sink: int) -> int:
    
    parent = [-1] * (len(graph))
    max_flow = 0

    
    while breadth_first_search(graph, source, sink, parent):
        path_flow = int(1e9)  
        s = sink

        while s != source:
            
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{ford_fulkerson(graph, source=0, sink=5) = }")
