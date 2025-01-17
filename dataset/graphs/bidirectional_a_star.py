
from __future__ import annotations

import time
from math import sqrt


HEURISTIC = 0

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

TPosition = tuple[int, int]


class Node:

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        goal_x: int,
        goal_y: int,
        g_cost: int,
        parent: Node | None,
    ) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_y, pos_x)
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.g_cost = g_cost
        self.parent = parent
        self.h_cost = self.calculate_heuristic()
        self.f_cost = self.g_cost + self.h_cost

    def calculate_heuristic(self) -> float:
        dy = self.pos_x - self.goal_x
        dx = self.pos_y - self.goal_y
        if HEURISTIC == 1:
            return abs(dx) + abs(dy)
        else:
            return sqrt(dy**2 + dx**2)

    def __lt__(self, other: Node) -> bool:
        return self.f_cost < other.f_cost


class AStar:

    def __init__(self, start: TPosition, goal: TPosition):
        self.start = Node(start[1], start[0], goal[1], goal[0], 0, None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], 99999, None)

        self.open_nodes = [self.start]
        self.closed_nodes: list[Node] = []

        self.reached = False

    def search(self) -> list[TPosition]:
        while self.open_nodes:
            
            self.open_nodes.sort()
            current_node = self.open_nodes.pop(0)

            if current_node.pos == self.target.pos:
                return self.retrace_path(current_node)

            self.closed_nodes.append(current_node)
            successors = self.get_successors(current_node)

            for child_node in successors:
                if child_node in self.closed_nodes:
                    continue

                if child_node not in self.open_nodes:
                    self.open_nodes.append(child_node)
                else:
                    
                    better_node = self.open_nodes.pop(self.open_nodes.index(child_node))

                    if child_node.g_cost < better_node.g_cost:
                        self.open_nodes.append(child_node)
                    else:
                        self.open_nodes.append(better_node)

        return [self.start.pos]

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
                Node(
                    pos_x,
                    pos_y,
                    self.target.pos_y,
                    self.target.pos_x,
                    parent.g_cost + 1,
                    parent,
                )
            )
        return successors

    def retrace_path(self, node: Node | None) -> list[TPosition]:
        current_node = node
        path = []
        while current_node is not None:
            path.append((current_node.pos_y, current_node.pos_x))
            current_node = current_node.parent
        path.reverse()
        return path


class BidirectionalAStar:

    def __init__(self, start: TPosition, goal: TPosition) -> None:
        self.fwd_astar = AStar(start, goal)
        self.bwd_astar = AStar(goal, start)
        self.reached = False

    def search(self) -> list[TPosition]:
        while self.fwd_astar.open_nodes or self.bwd_astar.open_nodes:
            self.fwd_astar.open_nodes.sort()
            self.bwd_astar.open_nodes.sort()
            current_fwd_node = self.fwd_astar.open_nodes.pop(0)
            current_bwd_node = self.bwd_astar.open_nodes.pop(0)

            if current_bwd_node.pos == current_fwd_node.pos:
                return self.retrace_bidirectional_path(
                    current_fwd_node, current_bwd_node
                )

            self.fwd_astar.closed_nodes.append(current_fwd_node)
            self.bwd_astar.closed_nodes.append(current_bwd_node)

            self.fwd_astar.target = current_bwd_node
            self.bwd_astar.target = current_fwd_node

            successors = {
                self.fwd_astar: self.fwd_astar.get_successors(current_fwd_node),
                self.bwd_astar: self.bwd_astar.get_successors(current_bwd_node),
            }

            for astar in [self.fwd_astar, self.bwd_astar]:
                for child_node in successors[astar]:
                    if child_node in astar.closed_nodes:
                        continue

                    if child_node not in astar.open_nodes:
                        astar.open_nodes.append(child_node)
                    else:
                        
                        better_node = astar.open_nodes.pop(
                            astar.open_nodes.index(child_node)
                        )

                        if child_node.g_cost < better_node.g_cost:
                            astar.open_nodes.append(child_node)
                        else:
                            astar.open_nodes.append(better_node)

        return [self.fwd_astar.start.pos]

    def retrace_bidirectional_path(
        self, fwd_node: Node, bwd_node: Node
    ) -> list[TPosition]:
        fwd_path = self.fwd_astar.retrace_path(fwd_node)
        bwd_path = self.bwd_astar.retrace_path(bwd_node)
        bwd_path.pop()
        bwd_path.reverse()
        path = fwd_path + bwd_path
        return path


if __name__ == "__main__":
    
    init = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    for elem in grid:
        print(elem)

    start_time = time.time()
    a_star = AStar(init, goal)
    path = a_star.search()
    end_time = time.time() - start_time
    print(f"AStar execution time = {end_time:f} seconds")

    bd_start_time = time.time()
    bidir_astar = BidirectionalAStar(init, goal)
    bd_end_time = time.time() - bd_start_time
    print(f"BidirectionalAStar execution time = {bd_end_time:f} seconds")
