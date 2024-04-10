def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    cache = [[0] * n for _ in range(m)]
    max_length = 0

    def dfs(i, j):
        if cache[i][j]:
            return cache[i][j]

        max_path = 1
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                max_path = max(max_path, dfs(x, y) + 1)

        cache[i][j] = max_path
        return max_path

    for i in range(m):
        for j in range(n):
            max_length = max(max_length, dfs(i, j))

    return max_length