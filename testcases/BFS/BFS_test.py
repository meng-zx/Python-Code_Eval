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

    def test_all_cells_same_letter(self):
        board = [["a", "a", "a"], ["a", "a", "a"], ["a", "a", "a"]]
        words = ["a", "aa", "aaa", "aaaa"]
        expected = ["a", "aa", "aaa"]
        self.assertCountEqual(findWords(board, words), expected)

    def test_word_subset_of_another(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["abc", "ab", "abcd"]
        expected = ["ab"]
        self.assertCountEqual(findWords(board, words), expected)

    def test_single_row_or_column_board(self):
        board = [["a", "b", "c", "d"]]
        words = ["ab", "bc", "cd", "abc", "abcd", "abcde"]
        expected = ["ab", "bc", "cd", "abc", "abcd"]
        self.assertCountEqual(findWords(board, words), expected)

        board = [["a"], ["b"], ["c"], ["d"]]
        words = ["ab", "bc", "cd", "abc", "abcd", "abcde"]
        self.assertCountEqual(findWords(board, words), expected)

    def test_diagonal_words_not_allowed(self):
        board = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
        words = ["aei", "beh", "cfi"]
        expected = []
        self.assertCountEqual(findWords(board, words), expected)

    def test_large_case_with_sparse_words(self):
        board = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s"],
                 ["d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b"],
                 ["n", "m", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                 ["a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c"],
                 ["v", "b", "n", "m", "q", "w", "e", "r", "t", "y", "u", "i"],
                 ["o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z"],
                 ["x", "c", "v", "b", "n", "m", "q", "w", "e", "r", "t", "y"],
                 ["u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k"],
                 ["l", "z", "x", "c", "v", "b", "n", "m", "q", "w", "e", "r"],
                 ["t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h"],
                 ["j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "q", "w"],
                 ["e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f"]]
        words = ["qwerty", "asdfgh", "zxcvbn", "qazwsx", "rfvtgb", "tgbnhy", "edcrfv"]
        expected = ["qwerty", "asdfgh", "zxcvbn", "qazwsx", "rfvtgb", "tgbnhy", "edcrfv"]
        self.assertCountEqual(findWords(board, words), expected)

    def test_words_with_nonexistent_letters(self):
        board = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
        words = ["jkl", "mnop", "qrst"]
        expected = []
        self.assertCountEqual(findWords(board, words), expected)

    def test_multiple_words_formed_from_same_path(self):
        board = [["c", "a", "t"], ["r", "a", "t"], ["t", "e", "e"]]
        words = ["cat", "cater", "art", "cart", "tee"]
        expected = ["cat", "art", "cart", "tee"]
        self.assertCountEqual(findWords(board, words), expected)

    # ... Add more as needed


if __name__ == "__main__":
    unittest.main()