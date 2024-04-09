import unittest
from Graph2D import longestIncreasingPath # Import the function from your script

class TestLongestIncreasingPath(unittest.TestCase):
    def test_example1(self):
        matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
        expected = 4
        self.assertEqual(longestIncreasingPath(matrix), expected)

    def test_example2(self):
        matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
        expected = 4
        self.assertEqual(longestIncreasingPath(matrix), expected)

    def test_example3(self):
        matrix = [[1]]
        expected = 1
        self.assertEqual(longestIncreasingPath(matrix), expected)

    def test_single_row(self):
        matrix = [[1, 2, 3, 4, 5]]
        expected = 5
        self.assertEqual(longestIncreasingPath(matrix), expected)

    def test_single_column(self):
        matrix = [[1], [2], [3], [4], [5]]
        expected = 5
        self.assertEqual(longestIncreasingPath(matrix), expected)

    def test_descending_path(self):
        matrix = [[5, 4, 3], [6, 5, 2], [7, 6, 1]]
        expected = 7
        self.assertEqual(longestIncreasingPath(matrix), expected)

    def test_no_increasing_path(self):
        matrix = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        expected = 1
        self.assertEqual(longestIncreasingPath(matrix), expected)

    def test_large_matrix(self):
        matrix = [[i + j for j in range(100)] for i in range(100)]
        expected = 199
        self.assertEqual(longestIncreasingPath(matrix), expected)

if __name__ == '__main__':
    unittest.main()
