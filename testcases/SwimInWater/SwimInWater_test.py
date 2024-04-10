import unittest
from SwimInWater import swim_in_water  # Import the function from your script

class TestSwimInWater(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(swim_in_water([[0,2],[1,3]]), 3)

    def test_example_2(self):
        self.assertEqual(swim_in_water([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]), 16)

    def test_single_element(self):
        self.assertEqual(swim_in_water([[0]]), 0)

    def test_two_elements(self):
        self.assertEqual(swim_in_water([[0, 1]]), 1)

    def test_diagonal_increasing(self):
        self.assertEqual(swim_in_water([[0, 2], [1, 3]]), 3)

    def test_large_values(self):
        self.assertEqual(swim_in_water([[999, 1000], [998, 997]]), 999)

    def test_all_same_values(self):
        self.assertEqual(swim_in_water([[5, 5], [5, 5]]), 5)

    def test_larger_grid(self):
        grid = [[i + j for j in range(5)] for i in range(5)]
        self.assertEqual(swim_in_water(grid), 8)

    def test_non_uniform_grid(self):
        self.assertEqual(swim_in_water([[3, 2], [0, 1]]), 3)

    def test_grid_with_large_numbers(self):
        grid = [[i * j for j in range(50)] for i in range(50)]
        self.assertEqual(swim_in_water(grid), 2450)

    def test_grid_with_zeros(self):
        self.assertEqual(swim_in_water([[0, 0, 0], [0, 1, 2], [0, 0, 0]]), 2)

    def test_grid_with_maximum_value(self):
        self.assertEqual(swim_in_water([[2500, 0], [0, 2500]]), 2500)

    def test_large_grid_linear_increase(self):
        grid = [[i * 50 + j for j in range(50)] for i in range(50)]
        self.assertEqual(swim_in_water(grid), 2450)

    def test_large_grid_decreasing(self):
        grid = [[50 * 50 - (i * 50 + j) for j in range(50)] for i in range(50)]
        self.assertEqual(swim_in_water(grid), 2500 - 1)

    def test_snake_like_path(self):
        grid = [
            [8,  7,  6,  5,  4],
            [9,  10, 11, 12, 3],
            [18, 17, 16, 13, 2],
            [19, 20, 15, 14, 1],
            [24, 23, 22, 21, 0]
        ]
        self.assertEqual(swim_in_water(grid), 24)

    def test_large_grid_with_holes(self):
        grid = [
            [0, 2, 2, 2, 3],
            [2, 2, 2, 3, 4],
            [2, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7]
        ]
        self.assertEqual(swim_in_water(grid), 7)

    def test_checkerboard_pattern_small(self):
        grid = [
            [0, 9, 2, 9],
            [9, 3, 9, 8],
            [4, 9, 6, 9],
            [9, 7, 9, 8]
        ]
        self.assertEqual(swim_in_water(grid), 9)

    def test_checkerboard_pattern_large(self):
        n = 10
        grid = [[(i+j) % n for j in range(n)] for i in range(n)]
        expected_time = n - 1
        self.assertEqual(swim_in_water(grid), expected_time)

    def test_increasing_spiral(self):
        grid = [
            [0, 1, 2, 3],
            [11, 12, 13, 4],
            [10, 15, 14, 5],
            [9, 8, 7, 6]
        ]
        self.assertEqual(swim_in_water(grid), 15)

    def test_decreasing_spiral(self):
        grid = [
            [15, 14, 13, 12],
            [2, 3, 4, 11],
            [1, 6, 5, 10],
            [0, 7, 8, 9]
        ]
        self.assertEqual(swim_in_water(grid), 15)

    def test_random_pattern_large(self):
        grid = [
            [10, 24, 23, 12, 5],
            [18, 0, 15, 8, 17],
            [20, 22, 21, 14, 3],
            [11, 6, 2, 1, 19],
            [16, 4, 13, 9, 7]
        ]
        self.assertEqual(swim_in_water(grid), 24)

    def test_grid_with_extremes(self):
        grid = [
            [0, 49, 48, 47],
            [1, 24, 25, 46],
            [2, 23, 26, 45],
            [3, 22, 27, 44],
            [4, 21, 20, 43],
            [5, 6, 7, 42],
            [16, 17, 18, 19],
            [15, 14, 13, 40],
            [36, 35, 34, 39],
            [37, 32, 31, 38]
        ]
        self.assertEqual(swim_in_water(grid), 49)



if __name__ == "__main__":
    unittest.main()