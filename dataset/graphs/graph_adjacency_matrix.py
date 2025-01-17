

from __future__ import annotations

import random
import unittest
from pprint import pformat
from typing import Generic, TypeVar

import pytest

T = TypeVar("T")


class GraphAdjacencyMatrix(Generic[T]):
    def __init__(
        self, vertices: list[T], edges: list[list[T]], directed: bool = True
    ) -> None:
        self.directed = directed
        self.vertex_to_index: dict[T, int] = {}
        self.adj_matrix: list[list[int]] = []

        
        edges = edges or []
        vertices = vertices or []

        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            if len(edge) != 2:
                msg = f"Invalid input: {edge} must have length 2."
                raise ValueError(msg)
            self.add_edge(edge[0], edge[1])

    def add_edge(self, source_vertex: T, destination_vertex: T) -> None:
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} or "
                f"{destination_vertex} does not exist"
            )
            raise ValueError(msg)
        if self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Incorrect input: The edge already exists between "
                f"{source_vertex} and {destination_vertex}"
            )
            raise ValueError(msg)

        
        u: int = self.vertex_to_index[source_vertex]
        v: int = self.vertex_to_index[destination_vertex]
        self.adj_matrix[u][v] = 1
        if not self.directed:
            self.adj_matrix[v][u] = 1

    def remove_edge(self, source_vertex: T, destination_vertex: T) -> None:
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} or "
                f"{destination_vertex} does not exist"
            )
            raise ValueError(msg)
        if not self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Incorrect input: The edge does NOT exist between "
                f"{source_vertex} and {destination_vertex}"
            )
            raise ValueError(msg)

        
        u: int = self.vertex_to_index[source_vertex]
        v: int = self.vertex_to_index[destination_vertex]
        self.adj_matrix[u][v] = 0
        if not self.directed:
            self.adj_matrix[v][u] = 0

    def add_vertex(self, vertex: T) -> None:
        if self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} already exists in this graph."
            raise ValueError(msg)

        
        for row in self.adj_matrix:
            row.append(0)

        
        self.adj_matrix.append([0] * (len(self.adj_matrix) + 1))
        self.vertex_to_index[vertex] = len(self.adj_matrix) - 1

    def remove_vertex(self, vertex: T) -> None:
        if not self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} does not exist in this graph."
            raise ValueError(msg)

        
        
        start_index = self.vertex_to_index[vertex]
        self.adj_matrix.pop(start_index)

        
        
        for lst in self.adj_matrix:
            lst.pop(start_index)

        
        self.vertex_to_index.pop(vertex)

        
        for inner_vertex in self.vertex_to_index:
            if self.vertex_to_index[inner_vertex] >= start_index:
                self.vertex_to_index[inner_vertex] = (
                    self.vertex_to_index[inner_vertex] - 1
                )

    def contains_vertex(self, vertex: T) -> bool:
        return vertex in self.vertex_to_index

    def contains_edge(self, source_vertex: T, destination_vertex: T) -> bool:
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} "
                f"or {destination_vertex} does not exist."
            )
            raise ValueError(msg)

        u = self.vertex_to_index[source_vertex]
        v = self.vertex_to_index[destination_vertex]
        return self.adj_matrix[u][v] == 1

    def clear_graph(self) -> None:
        self.vertex_to_index = {}
        self.adj_matrix = []

    def __repr__(self) -> str:
        first = "Adj Matrix:\n" + pformat(self.adj_matrix)
        second = "\nVertex to index mapping:\n" + pformat(self.vertex_to_index)
        return first + second


class TestGraphMatrix(unittest.TestCase):
    def __assert_graph_edge_exists_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        edge: list[int],
    ) -> None:
        assert undirected_graph.contains_edge(edge[0], edge[1])
        assert undirected_graph.contains_edge(edge[1], edge[0])
        assert directed_graph.contains_edge(edge[0], edge[1])

    def __assert_graph_edge_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        edge: list[int],
    ) -> None:
        assert not undirected_graph.contains_edge(edge[0], edge[1])
        assert not undirected_graph.contains_edge(edge[1], edge[0])
        assert not directed_graph.contains_edge(edge[0], edge[1])

    def __assert_graph_vertex_exists_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        vertex: int,
    ) -> None:
        assert undirected_graph.contains_vertex(vertex)
        assert directed_graph.contains_vertex(vertex)

    def __assert_graph_vertex_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        vertex: int,
    ) -> None:
        assert not undirected_graph.contains_vertex(vertex)
        assert not directed_graph.contains_vertex(vertex)

    def __generate_random_edges(
        self, vertices: list[int], edge_pick_count: int
    ) -> list[list[int]]:
        assert edge_pick_count <= len(vertices)

        random_source_vertices: list[int] = random.sample(
            vertices[0 : int(len(vertices) / 2)], edge_pick_count
        )
        random_destination_vertices: list[int] = random.sample(
            vertices[int(len(vertices) / 2) :], edge_pick_count
        )
        random_edges: list[list[int]] = []

        for source in random_source_vertices:
            for dest in random_destination_vertices:
                random_edges.append([source, dest])

        return random_edges

    def __generate_graphs(
        self, vertex_count: int, min_val: int, max_val: int, edge_pick_count: int
    ) -> tuple[GraphAdjacencyMatrix, GraphAdjacencyMatrix, list[int], list[list[int]]]:
        if max_val - min_val + 1 < vertex_count:
            raise ValueError(
                "Will result in duplicate vertices. Either increase "
                "range between min_val and max_val or decrease vertex count"
            )

        
        random_vertices: list[int] = random.sample(
            range(min_val, max_val + 1), vertex_count
        )
        random_edges: list[list[int]] = self.__generate_random_edges(
            random_vertices, edge_pick_count
        )

        
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=random_edges, directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=random_edges, directed=True
        )

        return undirected_graph, directed_graph, random_vertices, random_edges

    def test_init_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

        for edge in random_edges:
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )

        assert not undirected_graph.directed
        assert directed_graph.directed

    def test_contains_vertex(self) -> None:
        random_vertices: list[int] = random.sample(range(101), 20)

        
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=True
        )

        
        for num in range(101):
            assert (num in random_vertices) == undirected_graph.contains_vertex(num)
            assert (num in random_vertices) == directed_graph.contains_vertex(num)

    def test_add_vertices(self) -> None:
        random_vertices: list[int] = random.sample(range(101), 20)

        
        undirected_graph: GraphAdjacencyMatrix = GraphAdjacencyMatrix(
            vertices=[], edges=[], directed=False
        )
        directed_graph: GraphAdjacencyMatrix = GraphAdjacencyMatrix(
            vertices=[], edges=[], directed=True
        )

        
        for num in random_vertices:
            undirected_graph.add_vertex(num)

        for num in random_vertices:
            directed_graph.add_vertex(num)

        
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

    def test_remove_vertices(self) -> None:
        random_vertices: list[int] = random.sample(range(101), 20)

        
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=True
        )

        
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

            undirected_graph.remove_vertex(num)
            directed_graph.remove_vertex(num)

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, num
            )

    def test_add_and_remove_vertices_repeatedly(self) -> None:
        random_vertices1: list[int] = random.sample(range(51), 20)
        random_vertices2: list[int] = random.sample(range(51, 101), 20)

        
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices1, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices1, edges=[], directed=True
        )

        
        for i, _ in enumerate(random_vertices1):
            undirected_graph.add_vertex(random_vertices2[i])
            directed_graph.add_vertex(random_vertices2[i])

            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, random_vertices2[i]
            )

            undirected_graph.remove_vertex(random_vertices1[i])
            directed_graph.remove_vertex(random_vertices1[i])

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, random_vertices1[i]
            )

        
        for i, _ in enumerate(random_vertices1):
            undirected_graph.remove_vertex(random_vertices2[i])
            directed_graph.remove_vertex(random_vertices2[i])

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, random_vertices2[i]
            )

    def test_contains_edge(self) -> None:
        
        vertex_count = 20
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(vertex_count, 0, 100, 4)

        
        all_possible_edges: list[list[int]] = []
        for i in range(vertex_count - 1):
            for j in range(i + 1, vertex_count):
                all_possible_edges.append([random_vertices[i], random_vertices[j]])
                all_possible_edges.append([random_vertices[j], random_vertices[i]])

        
        for edge in all_possible_edges:
            if edge in random_edges:
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, edge
                )
            elif [edge[1], edge[0]] in random_edges:
                
                
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, [edge[1], edge[0]]
                )
            else:
                self.__assert_graph_edge_does_not_exist_check(
                    undirected_graph, directed_graph, edge
                )

    def test_add_edge(self) -> None:
        
        random_vertices: list[int] = random.sample(range(101), 15)
        random_edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)

        
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=True
        )

        
        for edge in random_edges:
            undirected_graph.add_edge(edge[0], edge[1])
            directed_graph.add_edge(edge[0], edge[1])
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )

    def test_remove_edge(self) -> None:
        
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        
        for edge in random_edges:
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )
            undirected_graph.remove_edge(edge[0], edge[1])
            directed_graph.remove_edge(edge[0], edge[1])
            self.__assert_graph_edge_does_not_exist_check(
                undirected_graph, directed_graph, edge
            )

    def test_add_and_remove_edges_repeatedly(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        
        more_random_edges: list[list[int]] = []

        while len(more_random_edges) != len(random_edges):
            edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)
            for edge in edges:
                if len(more_random_edges) == len(random_edges):
                    break
                elif edge not in more_random_edges and edge not in random_edges:
                    more_random_edges.append(edge)

        for i, _ in enumerate(random_edges):
            undirected_graph.add_edge(more_random_edges[i][0], more_random_edges[i][1])
            directed_graph.add_edge(more_random_edges[i][0], more_random_edges[i][1])

            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, more_random_edges[i]
            )

            undirected_graph.remove_edge(random_edges[i][0], random_edges[i][1])
            directed_graph.remove_edge(random_edges[i][0], random_edges[i][1])

            self.__assert_graph_edge_does_not_exist_check(
                undirected_graph, directed_graph, random_edges[i]
            )

    def test_add_vertex_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with pytest.raises(ValueError):
                undirected_graph.add_vertex(vertex)
            with pytest.raises(ValueError):
                directed_graph.add_vertex(vertex)

    def test_remove_vertex_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for i in range(101):
            if i not in random_vertices:
                with pytest.raises(ValueError):
                    undirected_graph.remove_vertex(i)
                with pytest.raises(ValueError):
                    directed_graph.remove_vertex(i)

    def test_add_edge_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for edge in random_edges:
            with pytest.raises(ValueError):
                undirected_graph.add_edge(edge[0], edge[1])
            with pytest.raises(ValueError):
                directed_graph.add_edge(edge[0], edge[1])

    def test_remove_edge_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        more_random_edges: list[list[int]] = []

        while len(more_random_edges) != len(random_edges):
            edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)
            for edge in edges:
                if len(more_random_edges) == len(random_edges):
                    break
                elif edge not in more_random_edges and edge not in random_edges:
                    more_random_edges.append(edge)

        for edge in more_random_edges:
            with pytest.raises(ValueError):
                undirected_graph.remove_edge(edge[0], edge[1])
            with pytest.raises(ValueError):
                directed_graph.remove_edge(edge[0], edge[1])

    def test_contains_edge_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with pytest.raises(ValueError):
                undirected_graph.contains_edge(vertex, 102)
            with pytest.raises(ValueError):
                directed_graph.contains_edge(vertex, 102)

        with pytest.raises(ValueError):
            undirected_graph.contains_edge(103, 102)
        with pytest.raises(ValueError):
            directed_graph.contains_edge(103, 102)


if __name__ == "__main__":
    unittest.main()
