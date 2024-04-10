import unittest
from SwimInWater import swim_in_water  # Import the function from your script

class TestSwimInWater(unittest.TestCase):

    def test_example_1(self):
        grid = [[0,2],[1,3]]
        expected = 3
        result = swim_in_water(grid)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_example_2(self):
        grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
        expected = 16
        result = swim_in_water(grid)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_single_cell(self):
        grid = [[0]]
        expected = 0
        result = swim_in_water(grid)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_linear_increase(self):
        grid = [[i + j for j in range(5)] for i in range(5)]
        expected = 4
        result = swim_in_water(grid)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_max_elevation(self):
        grid = [[24, 23, 22], [12, 13, 21], [11, 14, 20], [10, 15, 19], [9, 16, 18], [8, 17, 25], [7, 6, 5]]
        expected = 25
        result = swim_in_water(grid)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()