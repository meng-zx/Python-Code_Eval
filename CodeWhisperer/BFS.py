def search(board, i, j, word, index, visited):
    if index == len(word) and word[index:] == "":
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or visited[i][j] or board[i][j] != word[index]:
        return False

    visited[i][j] = True
    found = (search(board, i + 1, j, word, index + 1, visited) or
             search(board, i - 1, j, word, index + 1, visited) or
             search(board, i, j + 1, word, index + 1, visited) or
             search(board, i, j - 1, word, index + 1, visited))

    visited[i][j] = False
    return found


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    m, n = len(board), len(board[0])
    results = []

    for word in words:
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if search(board, i, j, word, 0, visited):
                    results.append(word)

    return results
