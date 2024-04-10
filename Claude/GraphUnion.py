from collections import defaultdict


def makeConnected(n, connections):
    if len(connections) < n - 1:
        return -1  # Not enough connections to connect all computers

    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    components = 0

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    for node in range(n):
        if node not in visited:
            components += 1
            dfs(node)

    return components - 1
