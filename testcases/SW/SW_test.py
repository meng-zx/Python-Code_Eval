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

    def test_large_k(self):
        nums = [i for i in range(1000)]
        self.assertEqual(maxSlidingWindow(nums, len(nums)), [999])

    def test_all_elements_same(self):
        self.assertEqual(maxSlidingWindow([2,2,2,2,2], 3), [2,2,2])

    def test_decreasing_order(self):
        self.assertEqual(maxSlidingWindow([5,4,3,2,1], 2), [5,4,3,2])

    def test_increasing_order(self):
        self.assertEqual(maxSlidingWindow([1,2,3,4,5], 3), [3,4,5])

    def test_k_equals_array_length(self):
        self.assertEqual(maxSlidingWindow([1,3,5,7,9], 5), [9])

    def test_k_is_one(self):
        self.assertEqual(maxSlidingWindow([1,3,5,7,9], 1), [1,3,5,7,9])

    def test_array_with_negative_numbers(self):
        self.assertEqual(maxSlidingWindow([-1,-3,-5,-7,-9], 3), [-1,-3,-5])

    def test_array_with_positive_and_negative_numbers(self):
        self.assertEqual(maxSlidingWindow([-2, 0, 2, -4, 4, -6, 6], 3), [2, 2, 4, 4, 6])

    def test_large_array(self):
        nums = list(range(100000))
        k = 50000
        expected = nums[k-1:]
        self.assertEqual(maxSlidingWindow(nums, k), expected)

    def test_zeros_in_array(self):
        self.assertEqual(maxSlidingWindow([0,0,0,0,1,0,0,0], 3), [0,0,1,1,1,0,0])

    def test_random_order_array(self):
        self.assertEqual(maxSlidingWindow([3,1,2,4,5,2,3,1], 4), [4,4,5,5,5])

    def test_window_size_two(self):
        self.assertEqual(maxSlidingWindow([1,2,3,2,1], 2), [2,3,3,2])

    def test_duplicate_maximums_inside_window(self):
        self.assertEqual(maxSlidingWindow([4,2,3,4,4,2,1], 3), [4,4,4,4,4])

    def test_moving_window_exposes_new_maximum(self):
        self.assertEqual(maxSlidingWindow([1,2,3,4,5], 2), [2,3,4,5])

    def test_array_with_ascending_and_descending_sections(self):
        self.assertEqual(maxSlidingWindow([1,2,3,4,3,2,1], 3), [3,4,4,4,3])

    # Edge Cases
    def test_negative_k(self):
        with self.assertRaises(ValueError):
            maxSlidingWindow([1,2,3,4,5], -1)

    def test_k_is_zero(self):
        with self.assertRaises(ValueError):
            maxSlidingWindow([1,2,3,4,5], 0)

    def test_array_as_none(self):
        with self.assertRaises(TypeError):
            maxSlidingWindow(None, 3)

    # Add additional tests based on the scenarios above as needed



    # This test might be too heavy for some environments, consider commenting out if it's not necessary
    # def test_large_input(self):
    #     large_input = list(range(10000)) + list(range(10000, 0, -1))
    #     k = 5000
    #     expected = list(range(4999, 15000))
    #     self.assertEqual(maxSlidingWindow(large_input, k), expected)

if __name__ == '__main__':
    unittest.main()