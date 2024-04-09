def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0

    def dfs(x, y):
        if memo[x][y]:
            return memo[x][y]
        length = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                length = max(length, 1 + dfs(nx, ny))
        memo[x][y] = length
        return length

    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]
    max_length = 0
    for i in range(m):
        for j in range(n):
            max_length = max(max_length, dfs(i, j))
    return max_length