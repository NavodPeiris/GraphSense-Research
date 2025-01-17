
from __future__ import annotations

graph = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}


class Graph:
    def __init__(self, graph: dict[str, list[str]], source_vertex: str) -> None:
        self.graph = graph
        
        self.parent: dict[str, str | None] = {}
        self.source_vertex = source_vertex

    def breath_first_search(self) -> None:
        visited = {self.source_vertex}
        self.parent[self.source_vertex] = None
        queue = [self.source_vertex]  

        while queue:
            vertex = queue.pop(0)
            for adjacent_vertex in self.graph[vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    self.parent[adjacent_vertex] = vertex
                    queue.append(adjacent_vertex)

    def shortest_path(self, target_vertex: str) -> str:
        if target_vertex == self.source_vertex:
            return self.source_vertex

        target_vertex_parent = self.parent.get(target_vertex)
        if target_vertex_parent is None:
            msg = (
                f"No path from vertex: {self.source_vertex} to vertex: {target_vertex}"
            )
            raise ValueError(msg)

        return self.shortest_path(target_vertex_parent) + f"->{target_vertex}"


if __name__ == "__main__":
    g = Graph(graph, "G")
    g.breath_first_search()
    print(g.shortest_path("D"))
    print(g.shortest_path("G"))
    print(g.shortest_path("Foo"))
