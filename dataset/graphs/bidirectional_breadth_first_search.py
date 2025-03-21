
from __future__ import annotations

import time

Path = list[tuple[int, int]]

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
]

delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  


class Node:
    def __init__(
        self, pos_x: int, pos_y: int, goal_x: int, goal_y: int, parent: Node | None
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_y, pos_x)
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.parent = parent


class BreadthFirstSearch:

    def __init__(self, start: tuple[int, int], goal: tuple[int, int]):
        self.start = Node(start[1], start[0], goal[1], goal[0], None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], None)

        self.node_queue = [self.start]
        self.reached = False

    def search(self) -> Path | None:
        while self.node_queue:
            current_node = self.node_queue.pop(0)

            if current_node.pos == self.target.pos:
                self.reached = True
                return self.retrace_path(current_node)

            successors = self.get_successors(current_node)

            for node in successors:
                self.node_queue.append(node)

        if not self.reached:
            return [self.start.pos]
        return None

    def get_successors(self, parent: Node) -> list[Node]:
        successors = []
        for action in delta:
            pos_x = parent.pos_x + action[1]
            pos_y = parent.pos_y + action[0]
            if not (0 <= pos_x <= len(grid[0]) - 1 and 0 <= pos_y <= len(grid) - 1):
                continue

            if grid[pos_y][pos_x] != 0:
                continue

            successors.append(
                Node(pos_x, pos_y, self.target.pos_y, self.target.pos_x, parent)
            )
        return successors

    def retrace_path(self, node: Node | None) -> Path:
        current_node = node
        path = []
        while current_node is not None:
            path.append((current_node.pos_y, current_node.pos_x))
            current_node = current_node.parent
        path.reverse()
        return path


class BidirectionalBreadthFirstSearch:

    def __init__(self, start, goal):
        self.fwd_bfs = BreadthFirstSearch(start, goal)
        self.bwd_bfs = BreadthFirstSearch(goal, start)
        self.reached = False

    def search(self) -> Path | None:
        while self.fwd_bfs.node_queue or self.bwd_bfs.node_queue:
            current_fwd_node = self.fwd_bfs.node_queue.pop(0)
            current_bwd_node = self.bwd_bfs.node_queue.pop(0)

            if current_bwd_node.pos == current_fwd_node.pos:
                self.reached = True
                return self.retrace_bidirectional_path(
                    current_fwd_node, current_bwd_node
                )

            self.fwd_bfs.target = current_bwd_node
            self.bwd_bfs.target = current_fwd_node

            successors = {
                self.fwd_bfs: self.fwd_bfs.get_successors(current_fwd_node),
                self.bwd_bfs: self.bwd_bfs.get_successors(current_bwd_node),
            }

            for bfs in [self.fwd_bfs, self.bwd_bfs]:
                for node in successors[bfs]:
                    bfs.node_queue.append(node)

        if not self.reached:
            return [self.fwd_bfs.start.pos]
        return None

    def retrace_bidirectional_path(self, fwd_node: Node, bwd_node: Node) -> Path:
        fwd_path = self.fwd_bfs.retrace_path(fwd_node)
        bwd_path = self.bwd_bfs.retrace_path(bwd_node)
        bwd_path.pop()
        bwd_path.reverse()
        path = fwd_path + bwd_path
        return path


if __name__ == "__main__":
    
    import doctest

    doctest.testmod()
    init = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    for elem in grid:
        print(elem)

    start_bfs_time = time.time()
    bfs = BreadthFirstSearch(init, goal)
    path = bfs.search()
    bfs_time = time.time() - start_bfs_time

    print("Unidirectional BFS computation time : ", bfs_time)

    start_bd_bfs_time = time.time()
    bd_bfs = BidirectionalBreadthFirstSearch(init, goal)
    bd_path = bd_bfs.search()
    bd_bfs_time = time.time() - start_bd_bfs_time

    print("Bidirectional BFS computation time : ", bd_bfs_time)
