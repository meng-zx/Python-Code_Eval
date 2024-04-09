import unittest
from SW import maxSlidingWindow  # Import the function from your script

class TestMaxSlidingWindow(unittest.TestCase):
    def test_example1(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        expected = [3,3,5,5,6,7]
        self.assertEqual(maxSlidingWindow(nums, k), expected)

    def test_single_element(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertEqual(maxSlidingWindow(nums, k), expected)

    def test_all_equal_elements(self):
        nums = [2, 2, 2, 2]
        k = 2
        expected = [2, 2, 2]
        self.assertEqual(maxSlidingWindow(nums, k), expected)

    def test_window_size_equals_array_length(self):
        nums = [1, 3, 5, 7]
        k = 4
        expected = [7]
        self.assertEqual(maxSlidingWindow(nums, k), expected)

    def test_descending_and_ascending_order(self):
        nums_desc = [4, 3, 2, 1]
        k = 2
        expected_desc = [4, 3, 2]
        self.assertEqual(maxSlidingWindow(nums_desc, k), expected_desc)

        nums_asc = [1, 2, 3, 4]
        k = 2
        expected_asc = [2, 3, 4]
        self.assertEqual(maxSlidingWindow(nums_asc, k), expected_asc)

    def test_negative_numbers(self):
        nums = [-4, -2, -3, -1]
        k = 3
        expected = [-2, -1]
        self.assertEqual(maxSlidingWindow(nums, k), expected)

    def test_mixed_positive_negative_numbers(self):
        nums = [-1, 3, -1, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(maxSlidingWindow(nums, k), expected)

    def test_window_size_one(self):
        nums = [2, 1, 5, 3, 4]
        k = 1
        expected = [2, 1, 5, 3, 4]
        self.assertEqual(maxSlidingWindow(nums, k), expected)

    # This test might be too heavy for some environments, consider commenting out if it's not necessary
    # def test_large_input(self):
    #     large_input = list(range(10000)) + list(range(10000, 0, -1))
    #     k = 5000
    #     expected = list(range(4999, 15000))
    #     self.assertEqual(maxSlidingWindow(large_input, k), expected)

if __name__ == '__main__':
    unittest.main()