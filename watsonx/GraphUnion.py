class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False


def makeConnected(n, connections):
    if len(connections) < n - 1:
        return -1

    uf = UnionFind(n)

    extra_cables = 0
    for a, b in connections:
        if not uf.union(a, b):
            extra_cables += 1

    components = len({uf.find(i) for i in range(n)})

    return components - 1 if extra_cables >= components - 1 else -1