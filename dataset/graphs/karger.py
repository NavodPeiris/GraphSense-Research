
from __future__ import annotations

import random



TEST_GRAPH = {
    "1": ["2", "3", "4", "5"],
    "2": ["1", "3", "4", "5"],
    "3": ["1", "2", "4", "5", "10"],
    "4": ["1", "2", "3", "5", "6"],
    "5": ["1", "2", "3", "4", "7"],
    "6": ["7", "8", "9", "10", "4"],
    "7": ["6", "8", "9", "10", "5"],
    "8": ["6", "7", "9", "10"],
    "9": ["6", "7", "8", "10"],
    "10": ["6", "7", "8", "9", "3"],
}


def partition_graph(graph: dict[str, list[str]]) -> set[tuple[str, str]]:
    
    contracted_nodes = {node: {node} for node in graph}

    graph_copy = {node: graph[node][:] for node in graph}

    while len(graph_copy) > 2:
        
        u = random.choice(list(graph_copy.keys()))
        v = random.choice(graph_copy[u])

        
        uv = u + v
        uv_neighbors = list(set(graph_copy[u] + graph_copy[v]))
        uv_neighbors.remove(u)
        uv_neighbors.remove(v)
        graph_copy[uv] = uv_neighbors
        for neighbor in uv_neighbors:
            graph_copy[neighbor].append(uv)

        contracted_nodes[uv] = set(contracted_nodes[u].union(contracted_nodes[v]))

        
        del graph_copy[u]
        del graph_copy[v]
        for neighbor in uv_neighbors:
            if u in graph_copy[neighbor]:
                graph_copy[neighbor].remove(u)
            if v in graph_copy[neighbor]:
                graph_copy[neighbor].remove(v)

    
    groups = [contracted_nodes[node] for node in graph_copy]
    return {
        (node, neighbor)
        for node in groups[0]
        for neighbor in graph[node]
        if neighbor in groups[1]
    }


if __name__ == "__main__":
    print(partition_graph(TEST_GRAPH))
