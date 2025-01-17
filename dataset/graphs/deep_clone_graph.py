
from dataclasses import dataclass


@dataclass
class Node:
    value: int = 0
    neighbors: list["Node"] | None = None

    def __post_init__(self) -> None:
        self.neighbors = self.neighbors or []

    def __hash__(self) -> int:
        return id(self)


def clone_graph(node: Node | None) -> Node | None:
    if not node:
        return None

    originals_to_clones = {}  

    stack = [node]

    while stack:
        original = stack.pop()

        if original in originals_to_clones:
            continue

        originals_to_clones[original] = Node(original.value)

        stack.extend(original.neighbors or [])

    for original, clone in originals_to_clones.items():
        for neighbor in original.neighbors or []:
            cloned_neighbor = originals_to_clones[neighbor]

            if not clone.neighbors:
                clone.neighbors = []

            clone.neighbors.append(cloned_neighbor)

    return originals_to_clones[node]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
