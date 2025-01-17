
import heapq


def greedy_min_vertex_cover(graph: dict) -> set[int]:
    
    queue: list[list] = []

    
    
    
    for key, value in graph.items():
        
        heapq.heappush(queue, [-1 * len(value), (key, value)])

    
    chosen_vertices = set()

    
    
    while queue and queue[0][0] != 0:
        
        argmax = heapq.heappop(queue)[1][0]
        chosen_vertices.add(argmax)

        
        for elem in queue:
            
            if elem[0] == 0:
                continue
            
            
            if argmax in elem[1][1]:
                index = elem[1][1].index(argmax)
                del elem[1][1][index]
                elem[0] += 1
        
        heapq.heapify(queue)
    return chosen_vertices


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    graph = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    print(f"Minimum vertex cover:\n{greedy_min_vertex_cover(graph)}")
