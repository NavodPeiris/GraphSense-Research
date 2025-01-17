
demo_graph = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}


def bfs_shortest_path(graph: dict, start, goal) -> list[str]:
    
    explored = set()
    
    queue = [[start]]

    
    if start == goal:
        return [start]

    
    while queue:
        
        path = queue.pop(0)
        
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    return new_path

            
            explored.add(node)

    
    return []


def bfs_shortest_path_distance(graph: dict, start, target) -> int:
    if not graph or start not in graph or target not in graph:
        return -1
    if start == target:
        return 0
    queue = [start]
    visited = set(start)
    
    dist = {start: 0, target: -1}
    while queue:
        node = queue.pop(0)
        if node == target:
            dist[target] = (
                dist[node] if dist[target] == -1 else min(dist[target], dist[node])
            )
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
                dist[adjacent] = dist[node] + 1
    return dist[target]


if __name__ == "__main__":
    print(bfs_shortest_path(demo_graph, "G", "D"))  
    print(bfs_shortest_path_distance(demo_graph, "G", "D"))
