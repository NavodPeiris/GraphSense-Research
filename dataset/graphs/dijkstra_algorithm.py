



import math
import sys




class PriorityQueue:
    
    def __init__(self):
        self.cur_size = 0
        self.array = []
        self.pos = {}  

    def is_empty(self):
        return self.cur_size == 0

    def min_heapify(self, idx):
        lc = self.left(idx)
        rc = self.right(idx)
        if lc < self.cur_size and self.array(lc)[0] < self.array[idx][0]:
            smallest = lc
        else:
            smallest = idx
        if rc < self.cur_size and self.array(rc)[0] < self.array[smallest][0]:
            smallest = rc
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def insert(self, tup):
        self.pos[tup[1]] = self.cur_size
        self.cur_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1]), tup[0])

    def extract_min(self):
        min_node = self.array[0][1]
        self.array[0] = self.array[self.cur_size - 1]
        self.cur_size -= 1
        self.min_heapify(1)
        del self.pos[min_node]
        return min_node

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def par(self, i):
        return math.floor(i / 2)

    def swap(self, i, j):
        self.pos[self.array[i][1]] = j
        self.pos[self.array[j][1]] = i
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def decrease_key(self, tup, new_d):
        idx = self.pos[tup[1]]
        
        self.array[idx] = (new_d, tup[1])
        while idx > 0 and self.array[self.par(idx)][0] > self.array[idx][0]:
            self.swap(idx, self.par(idx))
            idx = self.par(idx)


class Graph:
    def __init__(self, num):
        self.adjList = {}  
        self.num_nodes = num  
        
        self.dist = [0] * self.num_nodes
        self.par = [-1] * self.num_nodes  

    def add_edge(self, u, v, w):
        
        if u in self.adjList:
            self.adjList[u].append((v, w))
        else:
            self.adjList[u] = [(v, w)]

        
        if v in self.adjList:
            self.adjList[v].append((u, w))
        else:
            self.adjList[v] = [(u, w)]

    def show_graph(self):
        for u in self.adjList:
            print(u, "->", " -> ".join(str(f"{v}({w})") for v, w in self.adjList[u]))

    def dijkstra(self, src):
        
        self.par = [-1] * self.num_nodes
        
        self.dist[src] = 0
        q = PriorityQueue()
        q.insert((0, src))  
        for u in self.adjList:
            if u != src:
                self.dist[u] = sys.maxsize  
                self.par[u] = -1

        while not q.is_empty():
            u = q.extract_min()  
            
            
            for v, w in self.adjList[u]:
                new_dist = self.dist[u] + w
                if self.dist[v] > new_dist:
                    if self.dist[v] == sys.maxsize:
                        q.insert((new_dist, v))
                    else:
                        q.decrease_key((self.dist[v], v), new_dist)
                    self.dist[v] = new_dist
                    self.par[v] = u

        
        self.show_distances(src)

    def show_distances(self, src):
        print(f"Distance from node: {src}")
        for u in range(self.num_nodes):
            print(f"Node {u} has distance: {self.dist[u]}")

    def show_path(self, src, dest):
        path = []
        cost = 0
        temp = dest
        
        while self.par[temp] != -1:
            path.append(temp)
            if temp != src:
                for v, w in self.adjList[temp]:
                    if v == self.par[temp]:
                        cost += w
                        break
            temp = self.par[temp]
        path.append(src)
        path.reverse()

        print(f"----Path to reach {dest} from {src}----")
        for u in path:
            print(f"{u}", end=" ")
            if u != dest:
                print("-> ", end="")

        print("\nTotal cost of path: ", cost)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    graph.show_graph()
    graph.dijkstra(0)
    graph.show_path(0, 4)
