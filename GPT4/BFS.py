from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()

    # Build the Trie from the list of words
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def dfs(node, i, j, path, result):
        if node.is_end_of_word:
            result.add(path)
            node.is_end_of_word = False  # Avoid duplicate entries

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return

        tmp, board[i][j] = board[i][j], "#"  # Mark the cell as visited
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            dfs(node.children[tmp], x, y, path + tmp, result)
        board[i][j] = tmp  # Reset the cell

    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(root, i, j, "", result)

    return list(result)
