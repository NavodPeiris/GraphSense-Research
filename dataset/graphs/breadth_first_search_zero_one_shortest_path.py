
from __future__ import annotations

from collections import deque
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Edge:

    destination_vertex: int
    weight: int


class AdjacencyList:

    def __init__(self, size: int):
        self._graph: list[list[Edge]] = [[] for _ in range(size)]
        self._size = size

    def __getitem__(self, vertex: int) -> Iterator[Edge]:
        return iter(self._graph[vertex])

    @property
    def size(self):
        return self._size

    def add_edge(self, from_vertex: int, to_vertex: int, weight: int):
        if weight not in (0, 1):
            raise ValueError("Edge weight must be either 0 or 1.")

        if to_vertex < 0 or to_vertex >= self.size:
            raise ValueError("Vertex indexes must be in [0; size).")

        self._graph[from_vertex].append(Edge(to_vertex, weight))

    def get_shortest_path(self, start_vertex: int, finish_vertex: int) -> int | None:
        queue = deque([start_vertex])
        distances: list[int | None] = [None] * self.size
        distances[start_vertex] = 0

        while queue:
            current_vertex = queue.popleft()
            current_distance = distances[current_vertex]
            if current_distance is None:
                continue

            for edge in self[current_vertex]:
                new_distance = current_distance + edge.weight
                dest_vertex_distance = distances[edge.destination_vertex]
                if (
                    isinstance(dest_vertex_distance, int)
                    and new_distance >= dest_vertex_distance
                ):
                    continue
                distances[edge.destination_vertex] = new_distance
                if edge.weight == 0:
                    queue.appendleft(edge.destination_vertex)
                else:
                    queue.append(edge.destination_vertex)

        if distances[finish_vertex] is None:
            raise ValueError("No path from start_vertex to finish_vertex.")

        return distances[finish_vertex]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
