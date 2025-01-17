
from heapq import heappop, heappush

import numpy as np


def dijkstra(
    grid: np.ndarray,
    source: tuple[int, int],
    destination: tuple[int, int],
    allow_diagonal: bool,
) -> tuple[float | int, list[tuple[int, int]]]:
    rows, cols = grid.shape
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if allow_diagonal:
        dx += [-1, -1, 1, 1]
        dy += [-1, 1, -1, 1]

    queue, visited = [(0, source)], set()
    matrix = np.full((rows, cols), np.inf)
    matrix[source] = 0
    predecessors = np.empty((rows, cols), dtype=object)
    predecessors[source] = None

    while queue:
        (dist, (x, y)) = heappop(queue)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == destination:
            path = []
            while (x, y) != source:
                path.append((x, y))
                x, y = predecessors[x, y]
            path.append(source)  
            path.reverse()
            return float(matrix[destination]), path

        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols:
                next_node = grid[nx][ny]
                if next_node == 1 and matrix[nx, ny] > dist + 1:
                    heappush(queue, (dist + 1, (nx, ny)))
                    matrix[nx, ny] = dist + 1
                    predecessors[nx, ny] = (x, y)

    return np.inf, []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
