
from __future__ import annotations

from typing import Any


class Graph:
    def __init__(self, num_of_nodes: int) -> None:

        self.m_num_of_nodes = num_of_nodes
        self.m_edges: list[list[int]] = []
        self.m_component: dict[int, int] = {}

    def add_edge(self, u_node: int, v_node: int, weight: int) -> None:

        self.m_edges.append([u_node, v_node, weight])

    def find_component(self, u_node: int) -> int:

        if self.m_component[u_node] == u_node:
            return u_node
        return self.find_component(self.m_component[u_node])

    def set_component(self, u_node: int) -> None:

        if self.m_component[u_node] != u_node:
            for k in self.m_component:
                self.m_component[k] = self.find_component(k)

    def union(self, component_size: list[int], u_node: int, v_node: int) -> None:

        
        component_size = []
        mst_weight = 0

        minimum_weight_edge: list[Any] = [-1] * self.m_num_of_nodes

        
        for node in range(self.m_num_of_nodes):
            self.m_component.update({node: node})
            component_size.append(1)

        num_of_components = self.m_num_of_nodes

        while num_of_components > 1:
            for edge in self.m_edges:
                u, v, w = edge

                u_component = self.m_component[u]
                v_component = self.m_component[v]

                if u_component != v_component:
                    

                    for component in (u_component, v_component):
                        if (
                            minimum_weight_edge[component] == -1
                            or minimum_weight_edge[component][2] > w
                        ):
                            minimum_weight_edge[component] = [u, v, w]

            for edge in minimum_weight_edge:
                if isinstance(edge, list):
                    u, v, w = edge

                    u_component = self.m_component[u]
                    v_component = self.m_component[v]

                    if u_component != v_component:
                        mst_weight += w
                        self.union(component_size, u_component, v_component)
                        print(f"Added edge [{u} - {v}]\nAdded weight: {w}\n")
                        num_of_components -= 1

            minimum_weight_edge = [-1] * self.m_num_of_nodes
        print(f"The total weight of the minimal spanning tree is: {mst_weight}")


def test_vector() -> None:
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
