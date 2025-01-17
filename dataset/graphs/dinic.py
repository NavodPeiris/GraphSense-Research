INF = float("inf")


class Dinic:
    def __init__(self, n):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]


    def add_edge(self, a, b, c, rcap=0):
        self.adj[a].append([b, len(self.adj[b]), c, 0])
        self.adj[b].append([a, len(self.adj[a]) - 1, rcap, 0])

    
    def depth_first_search(self, vertex, sink, flow):
        if vertex == sink or not flow:
            return flow

        for i in range(self.ptr[vertex], len(self.adj[vertex])):
            e = self.adj[vertex][i]
            if self.lvl[e[0]] == self.lvl[vertex] + 1:
                p = self.depth_first_search(e[0], sink, min(flow, e[2] - e[3]))
                if p:
                    self.adj[vertex][i][3] += p
                    self.adj[e[0]][e[1]][3] -= p
                    return p
            self.ptr[vertex] = self.ptr[vertex] + 1
        return 0

    
    def max_flow(self, source, sink):
        flow, self.q[0] = 0, source
        for l in range(31):  
            while True:
                self.lvl, self.ptr = [0] * len(self.q), [0] * len(self.q)
                qi, qe, self.lvl[source] = 0, 1, 1
                while qi < qe and not self.lvl[sink]:
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
                            self.q[qe] = e[0]
                            qe += 1
                            self.lvl[e[0]] = self.lvl[v] + 1

                p = self.depth_first_search(source, sink, INF)
                while p:
                    flow += p
                    p = self.depth_first_search(source, sink, INF)

                if not self.lvl[sink]:
                    break

        return flow





graph = Dinic(10)
source = 0
sink = 9
for vertex in range(1, 5):
    graph.add_edge(source, vertex, 1)
for vertex in range(5, 9):
    graph.add_edge(vertex, sink, 1)
for vertex in range(1, 5):
    graph.add_edge(vertex, vertex + 4, 1)


print(graph.max_flow(source, sink))
