from __future__ import annotations


class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def print_solution(self, distances_from_source: list[int]) -> None:
        print("Vertex \t Distance from Source")
        for vertex in range(self.vertices):
            print(vertex, "\t\t", distances_from_source[vertex])

    def minimum_distance(
        self, distances_from_source: list[int], visited: list[bool]
    ) -> int:

        
        minimum = 1e7
        min_index = 0

        
        for vertex in range(self.vertices):
            if distances_from_source[vertex] < minimum and visited[vertex] is False:
                minimum = distances_from_source[vertex]
                min_index = vertex
        return min_index

    def dijkstra(self, source: int) -> None:

        distances = [int(1e7)] * self.vertices  
        distances[source] = 0
        visited = [False] * self.vertices

        for _ in range(self.vertices):
            u = self.minimum_distance(distances, visited)
            visited[u] = True

            
            
            
            
            for v in range(self.vertices):
                if (
                    self.graph[u][v] > 0
                    and visited[v] is False
                    and distances[v] > distances[u] + self.graph[u][v]
                ):
                    distances[v] = distances[u] + self.graph[u][v]

        self.print_solution(distances)


if __name__ == "__main__":
    graph = Graph(9)
    graph.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0],
    ]
    graph.dijkstra(0)
