
def findWords(board, words) :
    if not board or not words:
        return []

    m, n = len(board), len(board[0])
    visited = [[False] * n for _ in range(m)]
    result = []

    def dfs(i, j, word, index):
        if index == len(word):
            result.append(word)
            return

        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[index]:
            return

        visited[i][j] = True
        dfs(i + 1, j, word, index + 1)
        dfs(i - 1, j, word, index + 1)
        dfs(i, j + 1, word, index + 1)
        dfs(i, j - 1, word, index + 1)
        visited[i][j] = False

    for word in words:
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(i, j, word, 0)

    return result
