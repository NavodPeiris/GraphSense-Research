



class Graph:
    def __init__(self):
        self.vertex = {}

    
    def print_graph(self) -> None:
        print(self.vertex)
        for i in self.vertex:
            print(i, " -> ", " -> ".join([str(j) for j in self.vertex[i]]))

    
    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        
        if from_vertex in self.vertex:
            self.vertex[from_vertex].append(to_vertex)
        else:
            
            self.vertex[from_vertex] = [to_vertex]

    def dfs(self) -> None:
        
        visited = [False] * len(self.vertex)

        
        for i in range(len(self.vertex)):
            if not visited[i]:
                self.dfs_recursive(i, visited)

    def dfs_recursive(self, start_vertex: int, visited: list) -> None:
        
        visited[start_vertex] = True

        print(start_vertex, end="")

        
        for i in self.vertex:
            if not visited[i]:
                print(" ", end="")
                self.dfs_recursive(i, visited)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.print_graph()
    print("DFS:")
    g.dfs()
