import unittest
from BFS import findWords  # Import the function from your script

class TestFindWords(unittest.TestCase):
    def test_example1(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        expected = {"eat", "oath"}
        result = set(findWords(board, words))
        self.assertEqual(result, expected)

    def test_example2(self):
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        expected = set()
        result = set(findWords(board, words))
        self.assertEqual(result, expected)

    def test_empty_board(self):
        board = []
        words = ["abc", "def"]
        expected = set()
        result = set(findWords(board, words))
        self.assertEqual(result, expected)

    def test_empty_words(self):
        board = [["a","b"],["c","d"]]
        words = []
        expected = set()
        result = set(findWords(board, words))
        self.assertEqual(result, expected)

    def test_single_character_board_and_word(self):
        board = [["a"]]
        words = ["a"]
        expected = {"a"}
        result = set(findWords(board, words))
        self.assertEqual(result, expected)

    def test_diagonal_non_adjacent(self):
        board = [["a", "b", "c"],
                 ["d", "e", "f"],
                 ["g", "h", "i"]]
        words = ["aei", "beh", "cfi"]
        expected = set()
        result = set(findWords(board, words))
        self.assertEqual(result, expected)

    def test_large_input(self):
        board = [["a", "a", "a", "a", "a", "a"],
                 ["a", "a", "a", "a", "a", "a"],
                 ["a", "a", "a", "a", "a", "a"],
                 ["a", "a", "a", "a", "a", "a"],
                 ["a", "a", "a", "a", "a", "a"],
                 ["a", "a", "a", "a", "a", "a"]]
        words = ["a" * 6, "a" * 7]
        expected = {"a" * 6}
        result = set(findWords(board, words))
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()