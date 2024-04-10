


def makeConnected(n, connections):
    connectivity = [[False] * n for _ in range(n)]

    unvisited = [True] * n

    for i in range(len(connections)):
        if unvisited[connections[i][0]] and unvisited[connections[i][1]]:
            connectivity[connections[i][0]] = True
            connectivity[connections[i][1]] = True

            unvisited[connections[i][0]] = False
            unvisited[connections[i][1]] = False

            for j in range(n):
                if unvisited[j] and not connectivity[j]:
                    connectivity[j] = True
                    unvisited[j] = False

    num_edges = 0
    for i in range(n):
        if connectivity[i]:
            num_edges += 1

    if num_edges == n * (n - 1) // 2:
        return 1
    else:
        return -1