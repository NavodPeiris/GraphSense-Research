
import random


def random_graph(
    vertices_number: int, probability: float, directed: bool = False
) -> dict:
    graph: dict = {i: [] for i in range(vertices_number)}

    
    if probability >= 1:
        return complete_graph(vertices_number)
    
    if probability <= 0:
        return graph

    
    
    for i in range(vertices_number):
        for j in range(i + 1, vertices_number):
            if random.random() < probability:
                graph[i].append(j)
                if not directed:
                    
                    graph[j].append(i)
    return graph


def complete_graph(vertices_number: int) -> dict:
    return {
        i: [j for j in range(vertices_number) if i != j] for i in range(vertices_number)
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()
