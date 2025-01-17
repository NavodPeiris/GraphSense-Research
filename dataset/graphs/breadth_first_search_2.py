
from __future__ import annotations

from collections import deque
from queue import Queue
from timeit import timeit

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def breadth_first_search(graph: dict, start: str) -> list[str]:
    explored = {start}
    result = [start]
    queue: Queue = Queue()
    queue.put(start)
    while not queue.empty():
        v = queue.get()
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                result.append(w)
                queue.put(w)
    return result


def breadth_first_search_with_deque(graph: dict, start: str) -> list[str]:
    visited = {start}
    result = [start]
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for child in graph[v]:
            if child not in visited:
                visited.add(child)
                result.append(child)
                queue.append(child)
    return result


def benchmark_function(name: str) -> None:
    setup = f"from __main__ import G, {name}"
    number = 10000
    res = timeit(f"{name}(G, 'A')", setup=setup, number=number)
    print(f"{name:<35} finished {number} runs in {res:.5f} seconds")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    benchmark_function("breadth_first_search")
    benchmark_function("breadth_first_search_with_deque")
