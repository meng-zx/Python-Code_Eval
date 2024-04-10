


def makeConnected(n, connections):
    graph = {}
    for c in connections:
        graph[c[0]] = graph.get(c[0], []) + [c[1]]
        graph[c[1]] = graph.get(c[1], []) + [c[0]]

    uf = UnionFind(n)
    for c in connections:
        uf.union(c[0], c[1])

        return -1

    min_connections = 0
    for i in range(n):
        for j in range(n):
            if i != j and uf.find(i) != uf.find(j):
                uf.union(i, j)
                min_connections += 1

                return min_connections


    return min_connections