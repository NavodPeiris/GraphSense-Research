
from __future__ import annotations

from sys import maxsize
from typing import Generic, TypeVar

T = TypeVar("T")


def get_parent_position(position: int) -> int:
    return (position - 1) // 2


def get_child_left_position(position: int) -> int:
    return (2 * position) + 1


def get_child_right_position(position: int) -> int:
    return (2 * position) + 2


class MinPriorityQueue(Generic[T]):

    def __init__(self) -> None:
        self.heap: list[tuple[T, int]] = []
        self.position_map: dict[T, int] = {}
        self.elements: int = 0

    def __len__(self) -> int:
        return self.elements

    def __repr__(self) -> str:
        return str(self.heap)

    def is_empty(self) -> bool:
        
        return self.elements == 0

    def push(self, elem: T, weight: int) -> None:
        
        self.heap.append((elem, weight))
        self.position_map[elem] = self.elements
        self.elements += 1
        self._bubble_up(elem)

    def extract_min(self) -> T:
        
        if self.elements > 1:
            self._swap_nodes(0, self.elements - 1)
        elem, _ = self.heap.pop()
        del self.position_map[elem]
        self.elements -= 1
        if self.elements > 0:
            bubble_down_elem, _ = self.heap[0]
            self._bubble_down(bubble_down_elem)
        return elem

    def update_key(self, elem: T, weight: int) -> None:
        
        position = self.position_map[elem]
        self.heap[position] = (elem, weight)
        if position > 0:
            parent_position = get_parent_position(position)
            _, parent_weight = self.heap[parent_position]
            if parent_weight > weight:
                self._bubble_up(elem)
            else:
                self._bubble_down(elem)
        else:
            self._bubble_down(elem)

    def _bubble_up(self, elem: T) -> None:
        
        
        curr_pos = self.position_map[elem]
        if curr_pos == 0:
            return None
        parent_position = get_parent_position(curr_pos)
        _, weight = self.heap[curr_pos]
        _, parent_weight = self.heap[parent_position]
        if parent_weight > weight:
            self._swap_nodes(parent_position, curr_pos)
            return self._bubble_up(elem)
        return None

    def _bubble_down(self, elem: T) -> None:
        
        
        curr_pos = self.position_map[elem]
        _, weight = self.heap[curr_pos]
        child_left_position = get_child_left_position(curr_pos)
        child_right_position = get_child_right_position(curr_pos)
        if child_left_position < self.elements and child_right_position < self.elements:
            _, child_left_weight = self.heap[child_left_position]
            _, child_right_weight = self.heap[child_right_position]
            if child_right_weight < child_left_weight and child_right_weight < weight:
                self._swap_nodes(child_right_position, curr_pos)
                return self._bubble_down(elem)
        if child_left_position < self.elements:
            _, child_left_weight = self.heap[child_left_position]
            if child_left_weight < weight:
                self._swap_nodes(child_left_position, curr_pos)
                return self._bubble_down(elem)
        else:
            return None
        if child_right_position < self.elements:
            _, child_right_weight = self.heap[child_right_position]
            if child_right_weight < weight:
                self._swap_nodes(child_right_position, curr_pos)
                return self._bubble_down(elem)
        return None

    def _swap_nodes(self, node1_pos: int, node2_pos: int) -> None:
        
        node1_elem = self.heap[node1_pos][0]
        node2_elem = self.heap[node2_pos][0]
        self.heap[node1_pos], self.heap[node2_pos] = (
            self.heap[node2_pos],
            self.heap[node1_pos],
        )
        self.position_map[node1_elem] = node2_pos
        self.position_map[node2_elem] = node1_pos


class GraphUndirectedWeighted(Generic[T]):

    def __init__(self) -> None:
        self.connections: dict[T, dict[T, int]] = {}
        self.nodes: int = 0

    def __repr__(self) -> str:
        return str(self.connections)

    def __len__(self) -> int:
        return self.nodes

    def add_node(self, node: T) -> None:
        
        if node not in self.connections:
            self.connections[node] = {}
            self.nodes += 1

    def add_edge(self, node1: T, node2: T, weight: int) -> None:
        
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1][node2] = weight
        self.connections[node2][node1] = weight


def prims_algo(
    graph: GraphUndirectedWeighted[T],
) -> tuple[dict[T, int], dict[T, T | None]]:
    
    dist: dict[T, int] = {node: maxsize for node in graph.connections}
    parent: dict[T, T | None] = {node: None for node in graph.connections}

    priority_queue: MinPriorityQueue[T] = MinPriorityQueue()
    for node, weight in dist.items():
        priority_queue.push(node, weight)

    if priority_queue.is_empty():
        return dist, parent

    
    node = priority_queue.extract_min()
    dist[node] = 0
    for neighbour in graph.connections[node]:
        if dist[neighbour] > dist[node] + graph.connections[node][neighbour]:
            dist[neighbour] = dist[node] + graph.connections[node][neighbour]
            priority_queue.update_key(neighbour, dist[neighbour])
            parent[neighbour] = node

    
    while not priority_queue.is_empty():
        node = priority_queue.extract_min()
        for neighbour in graph.connections[node]:
            if dist[neighbour] > dist[node] + graph.connections[node][neighbour]:
                dist[neighbour] = dist[node] + graph.connections[node][neighbour]
                priority_queue.update_key(neighbour, dist[neighbour])
                parent[neighbour] = node
    return dist, parent
