import unittest
from LIS import lengthOfLIS  # Import the function from your script

class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_example_2(self):
        self.assertEqual(lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)

    def test_example_3(self):
        self.assertEqual(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)

    def test_single_element(self):
        self.assertEqual(lengthOfLIS([10]), 1)

    def test_two_elements_increasing(self):
        self.assertEqual(lengthOfLIS([1, 2]), 2)

    def test_two_elements_decreasing(self):
        self.assertEqual(lengthOfLIS([2, 1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(lengthOfLIS([-1, -2, -3, -4, -5]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(lengthOfLIS([-10, -1, 0, 10, 20, 30]), 6)

    def test_large_input(self):
        self.assertEqual(lengthOfLIS(list(range(2500))), 2500)

    def test_large_input_reverse(self):
        self.assertEqual(lengthOfLIS(list(range(2500, 0, -1))), 1)

    def test_alternating_sequence(self):
        self.assertEqual(lengthOfLIS([1, 3, 2, 4, 3, 5]), 4)

    def test_repeating_elements_at_end(self):
        self.assertEqual(lengthOfLIS([1, 2, 3, 4, 4, 4, 4]), 4)

    def test_repeating_elements_at_start(self):
        self.assertEqual(lengthOfLIS([4, 4, 4, 4, 1, 2, 3]), 3)

    def test_all_negative_numbers(self):
        self.assertEqual(lengthOfLIS([-5, -4, -3, -2, -1]), 5)

    def test_empty_list(self):
        self.assertEqual(lengthOfLIS([]), 0)

    def test_random_case_1(self):
        self.assertEqual(lengthOfLIS([10, 22, 9, 33, 21, 50, 41, 60, 80]), 6)

    def test_random_case_2(self):
        self.assertEqual(lengthOfLIS([3, 10, 2, 1, 20]), 3)

    def test_sequence_with_one_increasing_element(self):
        self.assertEqual(lengthOfLIS([5, 4, 3, 2, 1, 6]), 2)

    def test_sequence_with_duplicates_and_increases(self):
        self.assertEqual(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]), 6)

    def test_very_large_input(self):
        large_input = [i % 500 for i in range(2500)]
        self.assertTrue(lengthOfLIS(large_input) > 1)

    def test_non_consecutive_increases(self):
        self.assertEqual(lengthOfLIS([10, 1, 2, 9, 3, 8, 4, 7, 5, 6]), 6)

    def test_decreasing_sequence(self):
        self.assertEqual(lengthOfLIS([5, 4, 3, 2, 1]), 1)

    def test_one_long_increasing_sequence_amidst_decreasing(self):
        self.assertEqual(lengthOfLIS([100, 1, 2, 3, 4, 0, -1, -2]), 5)

    def test_increasing_and_decreasing_sequence(self):
        self.assertEqual(lengthOfLIS([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]), 5)

    def test_all_same_elements_except_one(self):
        self.assertEqual(lengthOfLIS([1, 1, 1, 1, 2, 1, 1, 1]), 2)

    def test_sequence_with_large_numbers(self):
        self.assertEqual(lengthOfLIS([10000, 10001, 9999, 10002, 10003]), 4)

    def test_sequence_with_alternating_large_small_numbers(self):
        self.assertEqual(lengthOfLIS([1, 10000, 2, 10001, 3, 10002]), 4)

    def test_random_case_with_negatives(self):
        self.assertEqual(lengthOfLIS([-2, -1, -3, 4, 3, 5]), 3)

    def test_random_case_with_zeros(self):
        self.assertEqual(lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9]), 4)

if __name__ == "__main__":
    unittest.main()
