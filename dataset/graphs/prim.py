
import heapq as hq
import math
from collections.abc import Iterator


class Vertex:

    def __init__(self, id_):
        self.id = str(id_)
        self.key = None
        self.pi = None
        self.neighbors = []
        self.edges = {}  

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return self.id

    def add_neighbor(self, vertex):
        self.neighbors.append(vertex)

    def add_edge(self, vertex, weight):
        self.edges[vertex.id] = weight


def connect(graph, a, b, edge):
    
    graph[a - 1].add_neighbor(graph[b - 1])
    graph[b - 1].add_neighbor(graph[a - 1])
    
    graph[a - 1].add_edge(graph[b - 1], edge)
    graph[b - 1].add_edge(graph[a - 1], edge)


def prim(graph: list, root: Vertex) -> list:
    a = []
    for u in graph:
        u.key = math.inf
        u.pi = None
    root.key = 0
    q = graph[:]
    while q:
        u = min(q)
        q.remove(u)
        for v in u.neighbors:
            if (v in q) and (u.edges[v.id] < v.key):
                v.pi = u
                v.key = u.edges[v.id]
    for i in range(1, len(graph)):
        a.append((int(graph[i].id) + 1, int(graph[i].pi.id) + 1))
    return a


def prim_heap(graph: list, root: Vertex) -> Iterator[tuple]:
    for u in graph:
        u.key = math.inf
        u.pi = None
    root.key = 0

    h = list(graph)
    hq.heapify(h)

    while h:
        u = hq.heappop(h)
        for v in u.neighbors:
            if (v in h) and (u.edges[v.id] < v.key):
                v.pi = u
                v.key = u.edges[v.id]
                hq.heapify(h)

    for i in range(1, len(graph)):
        yield (int(graph[i].id) + 1, int(graph[i].pi.id) + 1)


def test_vector() -> None:
    pass

if __name__ == "__main__":
    import doctest

    doctest.testmod()
