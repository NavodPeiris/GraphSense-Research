


def _print_dist(dist, v):
    print("\nThe shortest path matrix using Floyd Warshall algorithm\n")
    for i in range(v):
        for j in range(v):
            if dist[i][j] != float("inf"):
                print(int(dist[i][j]), end="\t")
            else:
                print("INF", end="\t")
        print()


def floyd_warshall(graph, v):

    dist = [[float("inf") for _ in range(v)] for _ in range(v)]

    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]

            
    for k in range(v):
        
        for i in range(v):
            
            for j in range(v):
                if (
                    dist[i][k] != float("inf")
                    and dist[k][j] != float("inf")
                    and dist[i][k] + dist[k][j] < dist[i][j]
                ):
                    dist[i][j] = dist[i][k] + dist[k][j]

    _print_dist(dist, v)
    return dist, v


if __name__ == "__main__":
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    graph = [[float("inf") for i in range(v)] for j in range(v)]

    for i in range(v):
        graph[i][i] = 0.0

        
        
    for i in range(e):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:"))
        dst = int(input("Enter destination:"))
        weight = float(input("Enter weight:"))
        graph[src][dst] = weight

    floyd_warshall(graph, v)
