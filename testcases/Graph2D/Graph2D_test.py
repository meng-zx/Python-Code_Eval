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

    def test_empty_matrix(self):
        self.assertEqual(longestIncreasingPath([]), 0)

    # Test single row
    def test_single_row(self):
        self.assertEqual(longestIncreasingPath([[1, 2, 3, 4, 5]]), 5)

    # Test single column
    def test_single_column(self):
        self.assertEqual(longestIncreasingPath([[1], [2], [3], [4], [5]]), 5)

    # Test decreasing path
    def test_decreasing_path(self):
        self.assertEqual(longestIncreasingPath([[5, 4], [3, 2]]), 1)

    # Test matrix with same values
    def test_matrix_with_same_values(self):
        self.assertEqual(longestIncreasingPath([[1, 1], [1, 1]]), 1)

    # Test large matrix with 1 path
    def test_large_matrix_with_1_path(self):
        matrix = [[i for i in range(1, 201)] for _ in range(200)]
        self.assertEqual(longestIncreasingPath(matrix), 200)

    # Test path with turns
    def test_path_with_turns(self):
        matrix = [
            [1, 2, 3],
            [6, 5, 4],
            [7, 8, 9]
        ]
        self.assertEqual(longestIncreasingPath(matrix), 9)

    def test_large_matrix_minimal_path(self):
        matrix = [[200 - i if i % 2 == 0 else i for i in range(200)] for _ in range(200)]
        self.assertEqual(longestIncreasingPath(matrix), 2)

        # Test zigzag path

    def test_zigzag_path(self):
        matrix = [
            [7, 6, 1],
            [2, 3, 4],
            [1, 2, 3]
        ]
        self.assertEqual(longestIncreasingPath(matrix), 7)

        # Test matrix with large numbers

    def test_matrix_with_large_numbers(self):
        matrix = [
            [1, 2 ** 31 - 1],
            [2, 2 ** 30]
        ]
        self.assertEqual(longestIncreasingPath(matrix), 3)

        # Test matrix with isolated peaks

    def test_isolated_peaks(self):
        matrix = [
            [18, 13, 12, 11, 10],
            [17, 14, 3, 2, 9],
            [16, 15, 4, 1, 8],
            [19, 20, 5, 6, 7]
        ]
        self.assertEqual(longestIncreasingPath(matrix), 20)

        # Test uniform matrix except for one cell

    def test_uniform_except_one(self):
        matrix = [
            [1, 1, 1],
            [1, 2, 1],
            [1, 1, 1]
        ]
        self.assertEqual(longestIncreasingPath(matrix), 2)

        # Test with a large random matrix to evaluate performance
        # Note: This test might be too intensive for regular unit testing
        # def test_large_random_matrix(self):
        #     import random
        #     matrix = [[random.randint(1, 100) for _ in range(200)] for _ in range(200)]
        #     result = longestIncreasingPath(matrix)
        #     self.assertIsInstance(result, int)  # We are only checking if it executes without error

        # Test path around the edge of the matrix

    def test_path_around_edge(self):
        matrix = [
            [5, 4, 3],
            [6, 1, 2],
            [7, 8, 9]
        ]
        self.assertEqual(longestIncreasingPath(matrix), 9)

        # Test large square matrix with increasing diagonal

    def test_large_increasing_diagonal(self):
        size = 50
        matrix = [[j + 1 if i == j else 1 for j in range(size)] for i in range(size)]
        self.assertEqual(longestIncreasingPath(matrix), size)

if __name__ == '__main__':
    unittest.main()
