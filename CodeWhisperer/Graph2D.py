def longestIncreasingPath(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[-1] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            dp[i][j] = dfs(matrix, i, j, dp)

    return max(max(row) for row in dp)


def dfs(matrix, i, j, dp):
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 1
    for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + x, j + y
        dp[i][j] = max(dp[i][j], 1 + dfs(matrix, ni, nj, dp))
    return dp[i][j]