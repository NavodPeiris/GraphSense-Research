

edge_array = [
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'bh-e12', 'cd-e2', 'ce-e4',
     'de-e1', 'df-e8', 'dg-e5', 'dh-e10', 'ef-e3', 'eg-e2', 'fg-e6', 'gh-e6', 'hi-e3'],
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'cd-e2', 'de-e1', 'df-e8',
     'ef-e3', 'eg-e2', 'fg-e6'],
    ['ab-e1', 'ac-e3', 'bc-e4', 'bd-e2', 'de-e1', 'df-e8', 'dg-e5', 'ef-e3', 'eg-e2',
     'eh-e12', 'fg-e6', 'fh-e10', 'gh-e6'],
    ['ab-e1', 'ac-e3', 'bc-e4', 'bd-e2', 'bh-e12', 'cd-e2', 'df-e8', 'dh-e10'],
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'cd-e2', 'ce-e4', 'de-e1', 'df-e8',
     'dg-e5', 'ef-e3', 'eg-e2', 'fg-e6']
]



def get_distinct_edge(edge_array):
    distinct_edge = set()
    for row in edge_array:
        for item in row:
            distinct_edge.add(item[0])
    return list(distinct_edge)


def get_bitcode(edge_array, distinct_edge):
    bitcode = ["0"] * len(edge_array)
    for i, row in enumerate(edge_array):
        for item in row:
            if distinct_edge in item[0]:
                bitcode[i] = "1"
                break
    return "".join(bitcode)


def get_frequency_table(edge_array):
    distinct_edge = get_distinct_edge(edge_array)
    frequency_table = {}

    for item in distinct_edge:
        bit = get_bitcode(edge_array, item)
        
        
        s = bit.count("1")
        frequency_table[item] = [s, bit]
    
    sorted_frequency_table = [
        [k, v[0], v[1]]
        for k, v in sorted(frequency_table.items(), key=lambda v: v[1][0], reverse=True)
    ]
    return sorted_frequency_table


def get_nodes(frequency_table):
    nodes = {}
    for _, item in enumerate(frequency_table):
        nodes.setdefault(item[2], []).append(item[0])
    return nodes


def get_cluster(nodes):
    cluster = {}
    for key, value in nodes.items():
        cluster.setdefault(key.count("1"), {})[key] = value
    return cluster


def get_support(cluster):
    return [i * 100 / len(cluster) for i in cluster]


def print_all() -> None:
    print("\nNodes\n")
    for key, value in nodes.items():
        print(key, value)
    print("\nSupport\n")
    print(support)
    print("\n Cluster \n")
    for key, value in sorted(cluster.items(), reverse=True):
        print(key, value)
    print("\n Graph\n")
    for key, value in graph.items():
        print(key, value)
    print("\n Edge List of Frequent subgraphs \n")
    for edge_list in freq_subgraph_edge_list:
        print(edge_list)


def create_edge(nodes, graph, cluster, c1):
    for i in cluster[c1]:
        count = 0
        c2 = c1 + 1
        while c2 < max(cluster.keys()):
            for j in cluster[c2]:
                if int(i, 2) & int(j, 2) == int(i, 2):
                    if tuple(nodes[i]) in graph:
                        graph[tuple(nodes[i])].append(nodes[j])
                    else:
                        graph[tuple(nodes[i])] = [nodes[j]]
                    count += 1
            if count == 0:
                c2 = c2 + 1
            else:
                break


def construct_graph(cluster, nodes):
    x = cluster[max(cluster.keys())]
    cluster[max(cluster.keys()) + 1] = "Header"
    graph = {}
    for i in x:
        if (["Header"],) in graph:
            graph[(["Header"],)].append(x[i])
        else:
            graph[(["Header"],)] = [x[i]]
    for i in x:
        graph[(x[i],)] = [["Header"]]
    i = 1
    while i < max(cluster) - 1:
        create_edge(nodes, graph, cluster, i)
        i = i + 1
    return graph


def my_dfs(graph, start, end, path=None):
    path = (path or []) + [start]
    if start == end:
        paths.append(path)
    for node in graph[start]:
        if tuple(node) not in path:
            my_dfs(graph, tuple(node), end, path)


def find_freq_subgraph_given_support(s, cluster, graph):
    k = int(s / 100 * (len(cluster) - 1))
    for i in cluster[k]:
        my_dfs(graph, tuple(cluster[k][i]), (["Header"],))


def freq_subgraphs_edge_list(paths):
    freq_sub_el = []
    for edges in paths:
        el = []
        for j in range(len(edges) - 1):
            temp = list(edges[j])
            for e in temp:
                edge = (e[0], e[1])
                el.append(edge)
        freq_sub_el.append(el)
    return freq_sub_el


def preprocess(edge_array):
    for i in range(len(edge_array)):
        for j in range(len(edge_array[i])):
            t = edge_array[i][j].split("-")
            edge_array[i][j] = t


if __name__ == "__main__":
    preprocess(edge_array)
    frequency_table = get_frequency_table(edge_array)
    nodes = get_nodes(frequency_table)
    cluster = get_cluster(nodes)
    support = get_support(cluster)
    graph = construct_graph(cluster, nodes)
    find_freq_subgraph_given_support(60, cluster, graph)
    paths: list = []
    freq_subgraph_edge_list = freq_subgraphs_edge_list(paths)
    print_all()
